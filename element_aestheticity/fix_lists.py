import re

def fix_lists(text):
    # Fix the itemize at line 504
    # We want to insert \begin{paracol}{2} after \begin{itemize}
    # Then change every ODD \item to \item ... \switchcolumn
    # and every EVEN \item to \item ... \switchcolumn* (except the last one which doesn't need \switchcolumn*)
    
    def process_list(match):
        env = match.group(1) # itemize or enumerate
        content = match.group(2)
        
        # Split by \item
        items = re.split(r'\\item\b', content)
        if len(items) <= 1:
            return match.group(0)
            
        header = items[0]
        items = items[1:]
        
        new_content = header + "\\begin{paracol}{2}\n"
        for i, item in enumerate(items):
            new_content += "\\item" + item.rstrip() + "\n"
            if i < len(items) - 1:
                if i % 2 == 0:
                    new_content += "\\switchcolumn\n"
                else:
                    new_content += "\\switchcolumn*\n"
        new_content += "\\end{paracol}\n"
        return f"\\begin{{{env}}}{new_content}\\end{{{env}}}"

    text = re.sub(r'\\begin\{(itemize|enumerate)\}(.*?)\\end\{\1\}', process_list, text, flags=re.DOTALL)
    return text

if __name__ == '__main__':
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        text = f.read()
    text = fix_lists(text)
    with open('NQBH_element_aestheticity.tex', 'w', encoding='utf-8') as f:
        f.write(text)
