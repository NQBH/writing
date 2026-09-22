import re

with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
    text = f.read()

text = text.replace(r'\begin\{quote\}', r'\begin{quote}')
text = text.replace(r'\end\{quote\}', r'\end{quote}')
text = text.replace(r'\.\'\'', r".''")

with open('NQBH_element_aestheticity.tex', 'w', encoding='utf-8') as f:
    f.write(text)
