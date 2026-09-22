import re

with open("NQBH_element_aestheticity.tex", "r") as f:
    text = f.read()

# 1. Remove \usepackage{paracol}
text = re.sub(r'\\usepackage\{paracol\}\s*', '', text)

# 2. Remove \begin{paracol}{2} and \end{paracol}
text = re.sub(r'\\begin\{paracol\}\{2\}\s*', '', text)
text = re.sub(r'\\end\{paracol\}\s*', '', text)

# 3. Remove \switchcolumn and \switchcolumn[0]*
text = re.sub(r'\\switchcolumn(\[[0-9]+\]\*?)?\s*', '\n\n', text)

# 4. Collapse multiple newlines (3 or more) into exactly two
text = re.sub(r'\n{3,}', '\n\n', text)

with open("NQBH_element_aestheticity.tex", "w") as f:
    f.write(text)

