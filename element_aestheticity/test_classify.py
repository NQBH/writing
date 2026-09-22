import re

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
        
        if text.startswith("\\begin{", i):
            env_level += 1
        elif text.startswith("\\end{", i):
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

def is_vietnamese(text):
    # Heuristic: looking for some distinct Vietnamese characters outside of footnotes
    # Let's remove \footnote{...} to not be confused by translated footnotes
    # wait, regex to remove \footnote{...} is hard if nested. 
    # Just look for textsf{Bản dịch:} or standard vietnamese characters.
    # Actually, the English blocks don't have "à, ả, ã, á, ạ" etc outside of footnotes.
    # But footnotes DO contain them!
    # Let's just check if the text starts with a Vietnamese character or if we just alternate.
    pass

blocks = parse_blocks('NQBH_element_aestheticity.tex')
for idx, b in enumerate(blocks):
    b_stripped = b.strip()
    if b_stripped.startswith('\\section') or b_stripped.startswith('\\part'):
        print(f"{idx}: SECTION/PART")
    elif b_stripped.startswith('\\begin{center}') or b_stripped.startswith('\\begin{table}'):
        print(f"{idx}: SPANNING_ENV")
    else:
        print(f"{idx}: {b_stripped[:40].replace('\n', ' ')}")
