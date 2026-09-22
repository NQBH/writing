import re

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # 1. Add \usepackage{paracol}
    text = re.sub(r'(\\usepackage\[.*?\]\{vietnam\})', r'\1\n\\usepackage{paracol}', text)
    
    placeholders = {}
    counter = 0
    def repl_func(m):
        nonlocal counter
        ph = f"___PLACEHOLDER_{counter}___"
        placeholders[ph] = m.group(0)
        counter += 1
        return f"\n\n{ph}\n\n"
        
    text = re.sub(r'\\begin\{table\}.*?\\end\{table\}', repl_func, text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{center\}.*?\\end\{center\}', repl_func, text, flags=re.DOTALL)
    text = re.sub(r'\\begin\{tikzpicture\}.*?\\end\{tikzpicture\}', repl_func, text, flags=re.DOTALL)
    
    tags_to_isolate = [
        r'\\begin\{document\}', r'\\end\{document\}', r'\\maketitle', 
        r'\\begin\{abstract\}', r'\\end\{abstract\}', r'\\tableofcontents',
        r'\\part\{[^{}]*\}', r'\\section\{[^{}]*\}', r'\\subsection\{[^{}]*\}',
        r'\\emph\{Alignment Matrix Across Disciplines\}',
        r'\\emph\{Ma trận Gióng hàng Xuyên Kỷ luật\}',
        r'\\emph\{Halmosian Aesthetic Axis\}',
        r'\\emph\{Trục Thẩm mỹ Halmos\}',
        r'\\emph\{Pascalian Aesthetic Dimensions\}',
        r'\\emph\{Các Chiều kích Thẩm mỹ Pascal\}',
        r'\\emph\{Comparison of the Major Archetypes\}',
        r'\\emph\{Sự So sánh các Nguyên mẫu Chính\}',
        r'\\printbibliography(?:\[.*?\])?'
    ]
    for tag in tags_to_isolate:
        text = re.sub(r'(' + tag + r')', r'\n\n\1\n\n', text)
        
    text = re.sub(r'\n{3,}', '\n\n', text)
    blocks = text.split('\n\n')
    
    def remove_footnotes(t):
        while True:
            m = re.search(r'\\footnote\{', t)
            if not m: break
            start = m.start()
            brace_count = 0
            end = -1
            for i in range(start + 9, len(t)):
                if t[i] == '{': brace_count += 1
                elif t[i] == '}':
                    if brace_count == 0:
                        end = i
                        break
                    else: brace_count -= 1
            if end != -1: t = t[:start] + t[end+1:]
            else: break
        return t

    def is_vietnamese(t):
        t_clean = remove_footnotes(t)
        v_chars = set("ảãạắằẳẵặấầẩẫậếềểễệỉĩịỏõọốồổỗộớờởỡợủũụứừửữựỷỹỵ")
        count = sum(1 for c in t_clean.lower() if c in v_chars)
        return count > 0
        
    merged = []
    curr = ""
    for b in blocks:
        if curr: curr += "\n\n" + b
        else: curr = b
        brace_count = curr.count('{') - curr.count('}')
        if brace_count == 0:
            merged.append(curr)
            curr = ""
    if curr: merged.append(curr)
    blocks = merged
    
    out_blocks = []
    in_paracol = False
    
    def ensure_paracol():
        nonlocal in_paracol
        if not in_paracol:
            out_blocks.append("\\begin{paracol}{2}")
            in_paracol = True
            
    def end_paracol():
        nonlocal in_paracol
        if in_paracol:
            out_blocks.append("\\end{paracol}")
            in_paracol = False
            
    started_body = False
    
    for b in blocks:
        b_str = b.strip()
        if not b_str: continue
            
        if not started_body:
            out_blocks.append(b)
            if '\\begin{abstract}' in b_str or '\\tableofcontents' in b_str:
                started_body = True
            continue
            
        # Isolate tags or placeholders
        is_structural = False
        if "___PLACEHOLDER_" in b_str:
            is_structural = True
        else:
            for tag_regex in tags_to_isolate:
                if re.match(tag_regex, b_str):
                    is_structural = True
                    break
                    
        if is_structural:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if b_str.startswith('%'):
            out_blocks.append(b)
            continue
            
        if is_vietnamese(b_str):
            ensure_paracol()
            out_blocks.append("\\begin{rightcolumn}\n" + b + "\n\\end{rightcolumn}")
        else:
            ensure_paracol()
            out_blocks.append("\\begin{leftcolumn}\n" + b + "\n\\end{leftcolumn}")

    end_paracol()
    
    out_text = '\n\n'.join(out_blocks)
    for ph, orig in placeholders.items():
        out_text = out_text.replace(ph, orig)
        
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(out_text)

if __name__ == "__main__":
    process_file('NQBH_element_aestheticity.tex', 'NQBH_element_aestheticity.tex')
    print("Done")
