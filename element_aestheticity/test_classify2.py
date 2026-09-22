import re

def remove_footnotes(text):
    # simple recursive footnote removal
    while True:
        m = re.search(r'\\footnote\{', text)
        if not m:
            break
        start = m.start()
        # find matching brace
        brace_count = 0
        end = -1
        for i in range(start + 9, len(text)):
            if text[i] == '{':
                brace_count += 1
            elif text[i] == '}':
                if brace_count == 0:
                    end = i
                    break
                else:
                    brace_count -= 1
        if end != -1:
            text = text[:start] + text[end+1:]
        else:
            break
    return text

def is_vietnamese(text):
    text_no_fn = remove_footnotes(text)
    # Check for vietnamese specific characters
    vietnamese_chars = set("àáảãạăắằẳẵặâấầẩẫậđèéẻẽẹêếềểễệìíỉĩịòóỏõọôốồổỗộơớờởỡợùúủũụưứừửữựỳýỷỹỵ")
    count = sum(1 for c in text_no_fn.lower() if c in vietnamese_chars)
    return count > 5  # arbitrary threshold

def process_tex():
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = text.split('\n\n')
    merged_blocks = []
    
    # Merge blocks with mismatched braces or environments
    current_block = ""
    for b in blocks:
        if current_block:
            current_block += "\n\n" + b
        else:
            current_block = b
            
        brace_count = current_block.count('{') - current_block.count('}')
        env_tikz = current_block.count('\\begin{tikzpicture}') - current_block.count('\\end{tikzpicture}')
        env_center = current_block.count('\\begin{center}') - current_block.count('\\end{center}')
        env_table = current_block.count('\\begin{table}') - current_block.count('\\end{table}')
        
        if brace_count == 0 and env_tikz == 0 and env_center == 0 and env_table == 0:
            merged_blocks.append(current_block)
            current_block = ""
            
    if current_block:
        merged_blocks.append(current_block)

    # Let's print out the classification of the first 20 blocks
    for i, b in enumerate(merged_blocks):
        b_str = b.strip()
        if b_str.startswith('\\section') or b_str.startswith('\\part'):
            ctype = "SECTION"
        elif '\\begin{tikzpicture}' in b_str or '\\begin{table}' in b_str:
            ctype = "ENV"
        elif is_vietnamese(b_str):
            ctype = "VIETNAMESE"
        else:
            ctype = "ENGLISH"
            
        print(f"{i} [{ctype}]: {b_str[:50].replace(chr(10), ' ')}")

process_tex()
