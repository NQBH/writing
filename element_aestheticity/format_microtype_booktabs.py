import re

with open("NQBH_element_aestheticity.tex", "r") as f:
    content = f.read()

# Fix the tabular definitions to remove '|'
def remove_vertical_bars(match):
    # match.group(1) is the full string inside \begin{tabular}{...}
    cols = match.group(1)
    cols = cols.replace('|', '')
    return r'\begin{tabular}{@{}' + cols + r'@{}}'

content = re.sub(r'\\begin\{tabular\}\{([^{}]+(?:\{[^{}]+\}[^{}]*)*)\}', remove_vertical_bars, content)

with open("NQBH_element_aestheticity.tex", "w") as f:
    f.write(content)
