import sys

def analyze_tex(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        content = f.read()
    print(f"Total characters: {len(content)}")

if __name__ == "__main__":
    analyze_tex('NQBH_element_aestheticity.tex')
