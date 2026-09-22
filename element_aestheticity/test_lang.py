import re
import sys

def is_vietnamese(text):
    # Strip LaTeX commands like \emph{...} for cleaner matching
    t_clean = re.sub(r'\\[a-zA-Z]+\{.*?\}', '', text)
    # Some blocks are just math, they don't have text
    # But wait, math blocks that are duplicated might have `Tiện ích`
    v_words = ['và', 'trong', 'của', 'một', 'những', 'được', 'với', 'không', 'các', 'là', 'sự', 'để', 'như', 'khi', 'này', 'cho', 'tính', 'từ']
    # Also check for specific Vietnamese characters to be absolutely sure
    v_chars = set("ảãạắằẳẵặấầẩẫậếềểễệỉĩịỏõọốồổỗộớờởỡợủũụứừửữựỷỹỵáàâăđéèêíìóòôơúùưýỳ")
    
    count_chars = sum(1 for c in text.lower() if c in v_chars)
    if count_chars > 0:
        return True
        
    for w in v_words:
        if re.search(r'\b' + w + r'\b', text.lower()):
            return True
            
    return False

def test():
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Let's split by double newline
    blocks = content.split('\n\n')
    
    for b in blocks:
        b_clean = b.strip()
        if not b_clean: continue
        # Ignore structural blocks
        if any(b_clean.startswith(x) for x in ['\\part', '\\section', '\\subsection', '\\begin{table}', '\\end{table}', '\\begin{tikzpicture}', '\\end{tikzpicture}', '\\begin{center}', '\\end{center}']):
            continue
        
        # Test detection
        print(f"[{'VIE' if is_vietnamese(b_clean) else 'ENG'}] {b_clean[:60].replace(chr(10), ' ')}")

if __name__ == '__main__':
    test()
