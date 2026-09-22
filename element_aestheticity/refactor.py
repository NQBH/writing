import re
import sys

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        text = f.read()
        
    # 1. Add \usepackage{paracol} to the preamble
    text = re.sub(r'(\\usepackage\[.*?\]\{vietnam\})', r'\1\n\\usepackage{paracol}', text)
    
    # 2. Add blank lines around \section, \part, \begin{center}, \end{center}, \begin{table}[H], \end{table}
    # to ensure they are isolated blocks.
    # Be careful not to mess up existing blank lines too much (we can clean up multiple blank lines later)
    # We will isolate them.
    for tag in [r'\\part\{.*?\}', r'\\section\{.*?\}', 
                r'\\begin\{center\}', r'\\end\{center\}',
                r'\\begin\{table\}.*?', r'\\end\{table\}',
                r'\\begin\{tikzpicture\}.*?', r'\\end\{tikzpicture\}']:
        text = re.sub(r'(' + tag + r')', r'\n\n\1\n\n', text)
        
    # clean up excess blank lines
    text = re.sub(r'\n{3,}', '\n\n', text)
    
    # Now split into blocks
    blocks = text.split('\n\n')
    
    # Helper to remove footnotes for language detection
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
        # Unique Vietnamese characters (double diacritics, under-dots, etc.)
        v_chars = set("ảãạắằẳẵặấầẩẫậếềểễệỉĩịỏõọốồổỗộớờởỡợủũụứừửữựỷỹỵ")
        count = sum(1 for c in t_clean.lower() if c in v_chars)
        return count > 0
        
    # Merge blocks with mismatched braces
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
    
    # Now process blocks to emit the new document
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
            
    # We will only process blocks AFTER \begin{document}
    # Wait, \begin{abstract} requires paracol inside it.
    
    started_body = False
    
    for b in blocks:
        b_str = b.strip()
        
        # Pass through preamble and top-level commands
        if not started_body:
            out_blocks.append(b)
            if '\\begin{abstract}' in b_str:
                started_body = True
            continue
            
        # If we see \end{abstract}, we must end paracol before it (if open)
        if '\\end{abstract}' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if '\\tableofcontents' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        if b_str.startswith('%'):
            # Just output comments
            out_blocks.append(b)
            continue
            
        # Isolate structural / spanning blocks
        if (b_str.startswith('\\part') or b_str.startswith('\\section') or 
            b_str.startswith('\\begin{center}') or b_str.startswith('\\end{center}') or
            b_str.startswith('\\begin{table}') or b_str.startswith('\\end{table}') or
            b_str.startswith('\\begin{tikzpicture}') or b_str.startswith('\\end{tikzpicture}')):
            end_paracol()
            out_blocks.append(b)
            continue
            
        if '\\emph{Alignment Matrix Across Disciplines}' in b_str or '\\emph{Ma trận Gióng hàng Xuyên Kỷ luật}' in b_str:
            end_paracol()
            out_blocks.append(b)
            continue
            
        # Now it's a text block.
        # Is it Vietnamese or English?
        if is_vietnamese(b_str):
            ensure_paracol()
            out_blocks.append("\\begin{rightcolumn}\n" + b + "\n\\end{rightcolumn}")
        else:
            # Check if it's purely english or just some structural thing
            # If it's a completely empty block or just spacing, ignore or pass
            if not b_str:
                continue
            ensure_paracol()
            out_blocks.append("\\begin{leftcolumn}\n" + b + "\n\\end{leftcolumn}")

    # End paracol at the very end if still open
    end_paracol()
    
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write('\n\n'.join(out_blocks))

if __name__ == "__main__":
    process_file('NQBH_element_aestheticity.tex', 'NQBH_element_aestheticity_new.tex')
