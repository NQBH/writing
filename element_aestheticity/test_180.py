import re

def is_vietnamese(t):
    v_chars = set("ảãạắằẳẵặấầẩẫậếềểễệỉĩịỏõọốồổỗộớờởỡợủũụứừửữựỷỹỵáàâăđéèêíìóòôơúùưýỳ")
    return sum(1 for c in t.lower() if c in v_chars) > 2

with open('NQBH_element_aestheticity.tex') as f:
    text = f.read()

blocks = text.split('\n\n')
for i in range(180, 185):
    b = blocks[i].strip()
    if b:
        lang = 'VIE' if is_vietnamese(b) else 'ENG'
        print(f'{i}: [{lang}] {b[:60].replace(chr(10), " ")}')
