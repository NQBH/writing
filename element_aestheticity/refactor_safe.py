import re

def process_file(in_path, out_path):
    with open(in_path, 'r', encoding='utf-8') as f:
        text = f.read()

    # Add \usepackage{paracol} to the preamble
    if '\\usepackage{paracol}' not in text:
        text = re.sub(r'(\\usepackage\[.*?\]\{vietnam\})', r'\1\n\\usepackage{paracol}', text)

    # We want to isolate structural blocks so we can break around them.
    # Structural blocks that should span both columns:
    # \part, \section, \subsection
    # \begin{center} ... \end{center}
    # \begin{table} ... \end{table}
    # \begin{tikzpicture} ... \end{tikzpicture}
    # \begin{abstract} ... \end{abstract} -> wait, inside abstract we DO want paracol.
    # So we don't break abstract as a whole, we process inside it.
    
    # Let's write a block parser that respects curly braces and environments.
    blocks = []
    current_block = ""
    brace_level = 0
    
    # We will identify specific environments that should be kept together
    # like center, table, tikzpicture, itemize, quote, enumerate.
    # Wait, inside itemize, there ARE english and vietnamese items!
    # See lines 504-509:
    # \begin{itemize}
    # \item English
    # \item Vietnamese
    # \end{itemize}
    # If we keep itemize together, we can't paracol it properly!
    
    pass
