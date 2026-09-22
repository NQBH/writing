import re
import sys
import subprocess

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    text = re.sub(r'(\\usepackage\[.*?\]\{vietnam\})', r'\1\n\\usepackage{paracol}', text)
    
    # Isolate all these tags with blank lines so they form their own blocks
    tags_to_isolate = [
        r'\\begin\{document\}', r'\\maketitle', r'\\begin\{abstract\}', r'\\end\{abstract\}', r'\\tableofcontents',
        r'\\part\{.*?\}', r'\\section\{.*?\}', 
        r'\\begin\{center\}', r'\\end\{center\}',
        r'\\begin\{table\}.*?', r'\\end\{table\}',
        r'\\begin\{tikzpicture\}.*?', r'\\end\{tikzpicture\}',
        r'\\emph\{Alignment Matrix Across Disciplines\}',
        r'\\emph\{Ma trận Gióng hàng Xuyên Kỷ luật\}'
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
        if not b_str:
            continue
            
        if not started_body:
            out_blocks.append(b)
            if '\\begin{abstract}' in b_str or '\\tableofcontents' in b_str:
                started_body = True
            continue
            
        if '\\end{abstract}' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if '\\tableofcontents' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if b_str.startswith('%'):
            out_blocks.append(b)
            continue
            
        # Isolate structural blocks
        if (b_str.startswith('\\part') or b_str.startswith('\\section') or 
            b_str.startswith('\\begin{center}') or b_str.startswith('\\end{center}') or
            b_str.startswith('\\begin{table}') or b_str.startswith('\\end{table}') or
            b_str.startswith('\\begin{tikzpicture}') or b_str.startswith('\\end{tikzpicture}') or
            b_str.startswith('\\begin{document}') or b_str.startswith('\\maketitle') or
            b_str.startswith('\\emph{Alignment Matrix') or b_str.startswith('\\emph{Ma trận Gióng')):
            end_paracol()
            out_blocks.append(b)
            continue
            
        if is_vietnamese(b_str):
            ensure_paracol()
            out_blocks.append("\\begin{rightcolumn}\n" + b + "\n\\end{rightcolumn}")
        else:
            ensure_paracol()
            out_blocks.append("\\begin{leftcolumn}\n" + b + "\n\\end{leftcolumn}")

    end_paracol()
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(out_blocks))

if __name__ == "__main__":
    process_file('NQBH_element_aestheticity.tex', 'NQBH_element_aestheticity.tex')
    print("Done")
