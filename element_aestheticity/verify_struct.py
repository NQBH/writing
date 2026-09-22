import re

def verify_structure():
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        text = f.read()
        
    def remove_footnotes(t):
        while True:
            m = re.search(r'\\footnote\{', t)
            if not m: break
            start = m.start()
            brace_count = 0
            end = -1
            for i in range(start + 10, len(t)):
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
        v_chars = set("ảãạắằẳẵặấầẩẫậếềểễệỉĩịỏõọốồổỗộớờởỡợủũụứừửữựỷỹỵáàâăđéèêíìóòôơúùưýỳ")
        v_words = ['và', 'trong', 'của', 'một', 'những', 'được', 'với', 'không', 'các', 'là', 'sự', 'để', 'như', 'khi', 'này', 'cho', 'tính', 'từ', 'thể']
        
        count_chars = sum(1 for c in t_clean.lower() if c in v_chars)
        if count_chars > 2: return True
        
        for w in v_words:
            if re.search(r'\b' + w + r'\b', t_clean.lower()): return True
        return False

    blocks = text.split('\n\n')
    
    prev_lang = None
    
    for i, b in enumerate(blocks):
        b_str = b.strip()
        if not b_str: continue
        if any(b_str.startswith(x) for x in ['\\part', '\\section', '\\subsection', '\\begin{center}', '\\end{center}', '\\begin{table}', '\\end{table}', '\\begin{tikzpicture}', '\\end{tikzpicture}', '\\begin{abstract}', '\\end{abstract}', '\\begin{document}', '\\end{document}', '\\maketitle', '\\tableofcontents', '%', '\\title', '\\author', '\\date', '\\documentclass', '\\usepackage', '\\addbibresource', '\\renewcommand', '\\usetikzlibrary', '\\allowdisplaybreaks', '\\newtheorem', '\\def', '\\DeclareRobustCommand', '\\setlist', '\\printbibliography']):
            prev_lang = None
            continue
            
        lang = 'VIE' if is_vietnamese(b_str) else 'ENG'
        if lang == prev_lang:
            print(f"CONSECUTIVE {lang} at block {i}:")
            print(b_str[:100])
            print("---")
            
        prev_lang = lang

if __name__ == '__main__':
    verify_structure()
