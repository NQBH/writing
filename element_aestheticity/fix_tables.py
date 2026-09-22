with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

replacements = {
    # Table 1
    r"\emph{Domain} & \emph{Low Alignment State (Friction / Reflection)} & \emph{High Alignment State (Resonance / Fit)} \\":
    r"\emph{Domain} & \textbf{Low Alignment State (Friction / Reflection)} & \textbf{High Alignment State (Resonance / Fit)} \\",
    
    # Table 2
    r"\emph{Miền (Domain)} & \emph{Trạng thái Gióng hàng Thấp (Ma sát / Sự phản xạ)} & \emph{Trạng thái Gióng hàng Cao (Sự cộng hưởng / Khớp nối)} \\":
    r"\emph{Miền (Domain)} & \textbf{Trạng thái Gióng hàng Thấp (Ma sát / Sự phản xạ)} & \textbf{Trạng thái Gióng hàng Cao (Sự cộng hưởng / Khớp nối)} \\",
    
    # Table 3
    r"\emph{Dimension} & \emph{Obfuscated Formalism} & \emph{The Halmosian Canon} \\":
    r"\emph{Dimension} & \textbf{Obfuscated Formalism} & \textbf{The Halmosian Canon} \\",
    
    # Table 4
    r"\emph{Chiều kích (Dimension)} & \emph{Chủ nghĩa Hình thức Bị làm mờ (Obfuscated Formalism)} & \emph{Quy điển Halmos (The Halmosian Canon)} \\":
    r"\emph{Chiều kích (Dimension)} & \textbf{Chủ nghĩa Hình thức Bị làm mờ (Obfuscated Formalism)} & \textbf{Quy điển Halmos (The Halmosian Canon)} \\",
    
    # Table 5
    r"\emph{Aesthetic Form} & \emph{Core Pascalian Concept} & \emph{Philosophical Resonance} \\":
    r"\emph{Aesthetic Form} & \textbf{Core Pascalian Concept} & \textbf{Philosophical Resonance} \\",
    
    # Table 6
    r"\emph{Hình thái Thẩm mỹ (Aesthetic Form)} & \emph{Khái niệm Cốt lõi của Pascal (Core Pascalian Concept)} & \emph{Sự Cộng hưởng Triết học (Philosophical Resonance)} \\":
    r"\emph{Hình thái Thẩm mỹ (Aesthetic Form)} & \textbf{Khái niệm Cốt lõi của Pascal (Core Pascalian Concept)} & \textbf{Sự Cộng hưởng Triết học (Philosophical Resonance)} \\",
    
    # Table 7
    r"\emph{Dimension} & \emph{Alexander Grothendieck} & \emph{Terence Tao} \\":
    r"\emph{Dimension} & \textbf{Alexander Grothendieck} & \textbf{Terence Tao} \\",
    
    # Table 8
    r"\emph{Chiều kích (Dimension)} & \emph{Alexander Grothendieck} & \emph{Terence Tao} \\":
    r"\emph{Chiều kích (Dimension)} & \textbf{Alexander Grothendieck} & \textbf{Terence Tao} \\"
}

for old, new in replacements.items():
    if old not in text:
        print(f"NOT FOUND: {old}")
    text = text.replace(old, new)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Done.")
