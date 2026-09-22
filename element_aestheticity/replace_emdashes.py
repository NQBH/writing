import re

with open("NQBH_element_aestheticity.tex", "r") as f:
    lines = f.readlines()

def replace_emdashes(text):
    # A generic approach for multiple emdashes:
    # Often " --- " or "---" is used. We split by "---".
    # For sentences with exactly two emdashes, we use ( ).
    # If the text inside the emdash is a short phrase, ( ) is good.
    # Otherwise, we can just replace all with ", " and then fix spacing.
    pass

new_lines = []
for line in lines:
    if line.startswith("%") or "begin{tikzpicture}" in line or "end{tikzpicture}" in line:
        new_lines.append(line)
        continue
    
    c = line.count("---")
    if c == 0:
        new_lines.append(line)
        continue
        
    parts = line.split("---")
    new_line = parts[0]
    
    if c == 2:
        new_line = parts[0] + " (" + parts[1].strip() + ") " + parts[2].lstrip()
    elif c == 1:
        new_line = parts[0] + ", " + parts[1].lstrip()
    else:
        # > 2 emdashes in the same line
        # Let's just use ", " for all of them
        for i in range(1, len(parts)):
            new_line += ", " + parts[i].lstrip()
            
    # Fix potential punctuation issues like ", ." or ", ,"
    new_line = new_line.replace(", .", ".")
    new_line = new_line.replace(", ,", ",")
    new_line = new_line.replace("( ", "(")
    new_line = new_line.replace(" )", ")")
    
    new_lines.append(new_line)

with open("NQBH_element_aestheticity_cleaned.tex", "w") as f:
    f.writelines(new_lines)

