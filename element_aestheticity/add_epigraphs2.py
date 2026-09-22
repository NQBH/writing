with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

part1 = r"\part{The Aesthetics of Mathematical \& Logical Forms}"
part1_epigraph = r"""\part{The Aesthetics of Mathematical \& Logical Forms}

\vspace{0.5cm}
\begin{flushright}
    \begin{minipage}{0.65\textwidth}
        \textit{``A physical law must possess mathematical beauty. It is more important to have beauty in one's equations than to have them fit experiment.''} \\
        \textit{``Một định luật vật lý tất yếu phải sở hữu tính thẩm mỹ toán học. Việc bảo toàn vẻ đẹp trong các phương trình của ta còn trọng đại hơn việc ép buộc chúng phải thần phục các dữ kiện thực nghiệm.''} \\
        \vspace{1mm}
        \raggedleft \textsf{--- Paul A.M. Dirac}
    \end{minipage}
\end{flushright}
\vspace{1cm}"""

part2 = r"\part{The Aesthetics of Physical \& Human Realities}"
part2_epigraph = r"""\part{The Aesthetics of Physical \& Human Realities}

\vspace{0.5cm}
\begin{flushright}
    \begin{minipage}{0.65\textwidth}
        \textit{``The general struggle for existence of animate beings is not a struggle for raw materials, nor for basic energy, but a struggle for entropy.''} \\
        \textit{``Cuộc đấu tranh sinh tồn phổ quát của các hữu thể nhân sinh không nằm ở sự tranh đoạt nguyên liệu thô, cũng chẳng phải năng lượng nền tảng, mà là một cuộc tử chiến xoay quanh entropy.''} \\
        \vspace{1mm}
        \raggedleft \textsf{--- Ludwig Boltzmann}
    \end{minipage}
\end{flushright}
\vspace{1cm}"""

part3 = r"\part{Archetypes of the Mind (The Aesthetics of Genius)}"
part3_epigraph = r"""\part{Archetypes of the Mind (The Aesthetics of Genius)}

\vspace{0.5cm}
\begin{flushright}
    \begin{minipage}{0.65\textwidth}
        \textit{``It is in the nature of things that every true creation is born in solitude, and brought to term in solitude.''} \\
        \textit{``Bản tính của vạn vật quy định rằng: mọi sự kiến tạo đích thực đều phải hoài thai trong tĩnh mịch cô liêu, và đi đến điểm chung cuộc cũng trong chính sự cô liêu ấy.''} \\
        \vspace{1mm}
        \raggedleft \textsf{--- Alexander Grothendieck}
    \end{minipage}
\end{flushright}
\vspace{1cm}"""

text = text.replace(part1, part1_epigraph)
text = text.replace(part2, part2_epigraph)
text = text.replace(part3, part3_epigraph)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Done with replace.")
