import re

def fix_abstract(text):
    # \begin{abstract}
    # eng
    # vie
    # \end{abstract}
    
    def process_abstract(match):
        content = match.group(1).strip()
        parts = content.split('\n\n')
        if len(parts) == 2:
            return f"\\begin{{abstract}}\n\\begin{{paracol}}{{2}}\n{parts[0]}\n\\switchcolumn\n{parts[1]}\n\\end{{paracol}}\n\\end{{abstract}}"
        return match.group(0)

    text = re.sub(r'\\begin\{abstract\}(.*?)\\end\{abstract\}', process_abstract, text, flags=re.DOTALL)
    return text

if __name__ == '__main__':
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        text = f.read()
    text = fix_abstract(text)
    with open('NQBH_element_aestheticity.tex', 'w', encoding='utf-8') as f:
        f.write(text)
