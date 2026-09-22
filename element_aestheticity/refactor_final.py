import re

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
    count_chars = sum(1 for c in t_clean.lower() if c in v_chars)
    if count_chars > 2: return True
    v_words = ['và', 'trong', 'của', 'một', 'những', 'được', 'với', 'không', 'các', 'là', 'sự', 'để', 'như', 'khi', 'này', 'cho', 'tính', 'từ', 'thể']
    for w in v_words:
        if re.search(r'\b' + w + r'\b', t_clean.lower()): return True
    return False

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = []
    current_block = ""
    brace_level = 0
    env_level = 0
    
    i = 0
    while i < len(text):
        char = text[i]
        
        # We don't want to treat abstract, quote, paracol as environments that prevent splitting
        # because we want to split inside quote (if there are multiple) or we already fixed abstract/itemize
        # Wait! We already fixed abstract, itemize, enumerate!
        # If we just don't split inside ANY environment EXCEPT document, it might keep them together?
        # But wait, abstract is ALREADY fixed, and it contains \n\n. If we don't split inside abstract, the whole abstract is ONE block.
        # That's perfectly fine! It's a structural block!
        # Itemize and enumerate are ALREADY fixed, they are structural blocks!
        # What about quote?
        # The author wrote:
        # \begin{quote}
        # ENG
        # \end{quote}
        # \n\n
        # \begin{quote}
        # VIE
        # \end{quote}
        # These are TWO separate quote environments! So they WILL be split, because env_level goes to 0 between them!
        
        if text.startswith("\\begin{", i):
            # Find the environment name
            m = re.match(r'\\begin\{([^}]+)\}', text[i:])
            if m:
                env_name = m.group(1)
                if env_name != 'document':
                    env_level += 1
        elif text.startswith("\\end{", i):
            m = re.match(r'\\end\{([^}]+)\}', text[i:])
            if m:
                env_name = m.group(1)
                if env_name != 'document':
                    env_level -= 1
            
        if char == '{':
            if i == 0 or text[i-1] != '\\':
                brace_level += 1
        elif char == '}':
            if i == 0 or text[i-1] != '\\':
                brace_level -= 1
                
        current_block += char
        
        if char == '\n' and i + 1 < len(text) and text[i+1] == '\n':
            if brace_level == 0 and env_level == 0:
                blocks.append(current_block)
                current_block = ""
                while i + 1 < len(text) and text[i+1] == '\n':
                    i += 1
        i += 1
        
    if current_block:
        blocks.append(current_block)
        
    return blocks

def process_file(in_path, out_path):
    blocks = parse_blocks(in_path)
    
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
        
        if '\\begin{document}' in b_str:
            # We don't track env_level for document, so \begin{document} is its own block
            started_body = True
            out_blocks.append(b)
            continue
            
        if not started_body:
            out_blocks.append(b)
            continue
            
        if '\\end{document}' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if b_str.startswith('%'):
            out_blocks.append(b)
            continue
            
        is_structural = False
        structural_prefixes = [
            '\\part', '\\section', '\\subsection', '\\tableofcontents', '\\printbibliography',
            '\\begin{center}', '\\begin{table}', '\\begin{abstract}', '\\begin{itemize}', '\\begin{enumerate}'
        ]
        if any(b_str.startswith(p) for p in structural_prefixes):
            is_structural = True
            
        # Hardcode some known single-line structural/spanning things
        if '\\maketitle' in b_str:
            is_structural = True
            
        if is_structural:
            end_paracol()
            out_blocks.append(b)
            continue
            
        # Now it's a language block
        lang = 'VIE' if is_vietnamese(b_str) else 'ENG'
        
        ensure_paracol()
        
        if lang == 'ENG':
            out_blocks.append(f"\\switchcolumn[0]*\n{b}")
        else:
            out_blocks.append(f"\\switchcolumn\n{b}")
            
    # Add paracol package if not present in preamble
    out_text = '\n\n'.join(out_blocks)
    if '\\usepackage{paracol}' not in out_text:
        out_text = re.sub(r'(\\usepackage\[.*?\]\{vietnam\})', r'\1\n\\usepackage{paracol}', out_text)
        
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(out_text)

if __name__ == '__main__':
    process_file('NQBH_element_aestheticity.tex', 'NQBH_element_aestheticity_new.tex')
