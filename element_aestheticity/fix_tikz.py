with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

# Tikz 1
old_tikz_1 = r"""\begin{tikzpicture}[
    >=stealth, thick,
    block/.style={
        draw, rectangle, rounded corners=3mm,
        inner sep=8pt, align=center, font=\sffamily,
        top color=white
    },
    geo/.style={block, bottom color=blue!15, draw=blue!70!black},
    alg/.style={block, bottom color=red!15, draw=red!70!black}
]
    \node[geo, text width=6cm] (geo) at (0,0) {\emph{[ Geometric Intuition ]} \\ \emph{[ Trực giác Hình học ]} \\[1ex] \small Smooth Manifolds \& Spatial Flow \\ Đa tạp Trơn \& Dòng chảy Không gian};
    \node[alg, text width=6cm] (alg) at (8.5,0) {\emph{[ Algebraic Machinery ]} \\ \emph{[ Cỗ máy Đại số ]} \\[1ex] \small Differential Forms \& Rational CDGA \\ Các Dạng Vi phân \& CDGA Hữu tỉ};

    \draw[->, line width=1.5pt, draw=purple!70!black] (geo.east) to[out=25, in=155] node[midway, above, font=\footnotesize\bfseries, text=black, align=center] {Sullivan's Dictionary \\ Từ điển của Sullivan} (alg.west);
    \draw[<-, line width=1.5pt, draw=purple!70!black] (geo.east) to[out=-25, in=-155] node[midway, below, font=\footnotesize, text=gray!80!black, align=center] {Topological Invariants \\ Các Bất biến Tô-pô} (alg.west);
\end{tikzpicture}"""

new_tikz_1 = r"""\begin{tikzpicture}[
    >=stealth,
    block/.style={
        draw, rectangle,
        inner sep=8pt, align=center, font=\small
    }
]
    \node[block, text width=5cm] (geo) at (0,0) {\emph{Geometric intuition} \\ \emph{Trực giác hình học} \\[1ex] Smooth manifolds \& spatial flow \\ Đa tạp trơn \& dòng chảy không gian};
    \node[block, text width=5cm] (alg) at (8,0) {\emph{Algebraic machinery} \\ \emph{Cỗ máy đại số} \\[1ex] Differential forms \& rational CDGA \\ Các dạng vi phân \& CDGA hữu tỉ};

    \draw[->, thick] (geo.east) to[out=20, in=160] node[midway, above, font=\footnotesize, align=center] {Sullivan's dictionary \\ Từ điển của Sullivan} (alg.west);
    \draw[<-, thick] (geo.east) to[out=-20, in=-160] node[midway, below, font=\footnotesize, align=center] {Topological invariants \\ Các bất biến tô-pô} (alg.west);
\end{tikzpicture}"""

text = text.replace(old_tikz_1, new_tikz_1)

# Tikz 2
old_tikz_2 = r"""\begin{tikzpicture}[>=stealth, scale=1.5]
    % Flow channel shading
    \fill[cyan!15] (0,0) -- (1,0) -- (5,2.4) -- (5,3) -- (4,3) -- (0,0.6) -- cycle;
    
    % Anxiety and Boredom shading
    \fill[red!10] (0,0.6) -- (4,3) -- (0,3) -- cycle;
    \fill[orange!10] (1,0) -- (5,0) -- (5,2.4) -- cycle;

    % Axes
    \draw[->, thick] (0,0) -- (5.5,0) node[below, align=center] {Skill / Kỹ năng ($S$)};
    \draw[->, thick] (0,0) -- (0,3.5) node[above, rotate=90, anchor=south, xshift=-1.5cm, align=center] {challenge/thử thách ($C$)};

    % Labels
    \node[text=red!70!black, font=\bfseries, align=center] at (1.2, 2.4) {anxiety/lo âu};
    \node[text=orange!70!black, font=\bfseries, align=center] at (3.8, 0.6) {boredom/buồn tẻ, chán nản]};
    \node[text=blue!70!black, font=\bfseries, rotate=31, align=center] at (2.5, 1.5) {\emph{flow state/dòng chảy} \\ ($C \approx S$)};
    \node[text=gray!80!black, font=\bfseries, align=center] at (0.7, 0.35) {apathy/thờ ơ ]};
\end{tikzpicture}"""

new_tikz_2 = r"""\begin{tikzpicture}[>=stealth, scale=1.5]
    % Flow channel shading (using grayscale)
    \fill[black!10] (0,0) -- (1,0) -- (5,2.4) -- (5,3) -- (4,3) -- (0,0.6) -- cycle;
    
    % Axes
    \draw[->, thick] (0,0) -- (5.5,0) node[below, align=center] {Skill / Kỹ năng ($S$)};
    \draw[->, thick] (0,0) -- (0,3.5) node[above, rotate=90, anchor=south, xshift=-1.5cm, align=center] {Challenge / Thử thách ($C$)};

    % Labels
    \node[align=center, font=\small] at (1.2, 2.4) {Anxiety / Lo âu};
    \node[align=center, font=\small] at (3.8, 0.6) {Boredom / Buồn tẻ};
    \node[rotate=31, align=center, font=\small] at (2.5, 1.5) {\emph{Flow state / Dòng chảy} \\ ($C \approx S$)};
    \node[align=center, font=\small] at (0.8, 0.35) {Apathy / Thờ ơ};
\end{tikzpicture}"""

text = text.replace(old_tikz_2, new_tikz_2)

# Tikz 3
old_tikz_3 = r"""\begin{tikzpicture}[
    >=stealth, thick,
    box/.style={draw, rounded corners, inner sep=6pt, font=\sffamily, align=left},
    main/.style={box, fill=blue!10, draw=blue!50!black, font=\sffamily\bfseries},
    paren/.style={box, fill=green!10, draw=green!50!black},
    foot/.style={box, fill=orange!10, draw=orange!50!black},
    nested/.style={box, fill=red!10, draw=red!50!black}
]
    \node[main, anchor=west] (main) at (0, 3) {{[Main Prose: Linear Narrative]} \\ \textmd{{[Văn bản chính: Tự sự Tuyến tính]}}};
    \node[paren, anchor=west] (paren) at (1, 1.8) {(Parenthetical: Immediate self-correction) \\ (Phụ chú: Sự tự điều chỉnh tức thời)};
    \node[foot, anchor=west] (foot) at (1, 0.4) {{[Footnote: Recursive meta-audit]} \\ {[Chú thích: Kiểm toán đệ quy]}};
    \node[nested, anchor=west] (nested) at (2, -1.0) {(Nested sub-footnote: Audit of the audit) \\ (Chú thích lồng nhau: Kiểm toán của kiểm toán)};

    % Lines
    \draw[->, draw=blue!70!black, thick] (0.5, 2.5) |- (paren.west);
    \draw[->, draw=blue!70!black, thick] (0.5, 2.5) |- (foot.west);
    \draw[->, draw=orange!70!black, thick] (1.5, -0.1) |- (nested.west);
\end{tikzpicture}"""

new_tikz_3 = r"""\begin{tikzpicture}[
    >=stealth,
    box/.style={draw, rectangle, inner sep=6pt, align=left, font=\small}
]
    \node[box, anchor=west] (main) at (0, 3) {\textbf{Main prose: linear narrative} \\ Văn bản chính: tự sự tuyến tính};
    \node[box, anchor=west] (paren) at (1, 1.8) {Parenthetical: immediate self-correction \\ Phụ chú: sự tự điều chỉnh tức thời};
    \node[box, anchor=west] (foot) at (1, 0.4) {Footnote: recursive meta-audit \\ Chú thích: kiểm toán đệ quy};
    \node[box, anchor=west] (nested) at (2, -1.0) {Nested sub-footnote: audit of the audit \\ Chú thích lồng nhau: kiểm toán của kiểm toán};

    % Lines
    \draw[->, thick] (0.5, 2.5) |- (paren.west);
    \draw[->, thick] (0.5, 2.5) |- (foot.west);
    \draw[->, thick] (1.5, -0.1) |- (nested.west);
\end{tikzpicture}"""

text = text.replace(old_tikz_3, new_tikz_3)

# Tikz 4
old_tikz_4 = r"""\begin{tikzpicture}[
    >=stealth, thick,
    block/.style={
        draw, rectangle, rounded corners=3mm,
        inner sep=8pt, align=center,
        font=\sffamily, top color=white
    },
    macro/.style={block, bottom color=cyan!15, draw=cyan!70!black},
    spectral/.style={block, bottom color=violet!15, draw=violet!70!black},
    micro/.style={block, bottom color=orange!15, draw=orange!70!black}
]
    \node[macro, text width=5cm] (macro) at (0,0) {\emph{[Macro-Level Heuristic]} \\ \emph{[Trực giác Vĩ mô]} \\[1ex] \small (Water Waves / Sóng nước)};
    \node[spectral, text width=5cm] (spectral) at (6,0) {\emph{[Spectral Analysis]} \\ \emph{[Giải tích Phổ]} \\[1ex] \small (Wavelet Decompositions \\ Phân tích Wavelet)};
    \node[micro, text width=5cm] (micro) at (12,0) {\emph{[Micro-Level Bound]} \\ \emph{[Giới hạn Vi mô]} \\[1ex] \small (Pointwise Estimates \\ Các Ước lượng Từng điểm)};

    \draw[<->, line width=1.5pt, draw=gray!60] (macro) -- (spectral);
    \draw[<->, line width=1.5pt, draw=gray!60] (spectral) -- (micro);
\end{tikzpicture}"""

new_tikz_4 = r"""\begin{tikzpicture}[
    >=stealth,
    block/.style={
        draw, rectangle,
        inner sep=8pt, align=center, font=\small
    }
]
    \node[block, text width=3.5cm] (macro) at (0,0) {\emph{Macro-level heuristic} \\ \emph{Trực giác vĩ mô} \\[1ex] (Water waves \\ Sóng nước)};
    \node[block, text width=3.5cm] (spectral) at (5,0) {\emph{Spectral analysis} \\ \emph{Giải tích phổ} \\[1ex] (Wavelet decompositions \\ Phân tích wavelet)};
    \node[block, text width=3.5cm] (micro) at (10,0) {\emph{Micro-level bound} \\ \emph{Giới hạn vi mô} \\[1ex] (Pointwise estimates \\ Các ước lượng từng điểm)};

    \draw[<->, thick] (macro) -- (spectral);
    \draw[<->, thick] (spectral) -- (micro);
\end{tikzpicture}"""

text = text.replace(old_tikz_4, new_tikz_4)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

