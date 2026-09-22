import re
import sys

def parse_blocks(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        text = f.read()

    blocks = []
    current_block = ""
    brace_level = 0
    env_level = 0
    
    i = 0
    while i < len(text):
        char = text[i]
        
        # Check for environment begin/end to avoid splitting inside them
        # (Though usually they are at brace_level = 0, we still want to keep them intact if they have blank lines inside)
        # Actually, tikzpicture can have blank lines, but we can just use simple double newline if brace_level == 0
        # Wait, what if there's a blank line inside \begin{tikzpicture} ... \end{tikzpicture}?
        # Let's track \begin{...} and \end{...}
        
        if text.startswith("\\begin{", i):
            env_level += 1
        elif text.startswith("\\end{", i):
            env_level -= 1
            
        if char == '{':
            # Ignore \{
            if i == 0 or text[i-1] != '\\':
                brace_level += 1
        elif char == '}':
            if i == 0 or text[i-1] != '\\':
                brace_level -= 1
                
        current_block += char
        
        # Check for paragraph break
        if char == '\n' and i + 1 < len(text) and text[i+1] == '\n':
            # Next is also newline
            # Only break if brace_level == 0 and env_level == 0
            if brace_level == 0 and env_level == 0:
                blocks.append(current_block)
                current_block = ""
                # skip all following newlines
                while i + 1 < len(text) and text[i+1] == '\n':
                    i += 1
        i += 1
        
    if current_block:
        blocks.append(current_block)
        
    return blocks

if __name__ == "__main__":
    blocks = parse_blocks('NQBH_element_aestheticity.tex')
    print(f"Total blocks: {len(blocks)}")
    # Print the first few blocks to verify
    for i, b in enumerate(blocks[:20]):
        print(f"--- Block {i} ---")
        print(b.strip())
