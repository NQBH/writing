import re

def fix_missing_translation():
    with open('NQBH_element_aestheticity.tex', 'r', encoding='utf-8') as f:
        text = f.read()

    # Fix duplicated quote
    quote_eng = r'\\begin\{quote\}\n``All of man\'s unhappiness stems from one single fact: that he cannot sit quietly in his own room alone\.\'\'\n\\end\{quote\}'
    quote_dup = r'\\begin\{quote\}\n``All of man\'s unhappiness stems from one single fact: that he cannot sit quietly in his own room alone\.\'\\\n\\end\{quote\}'
    
    # We will just replace the sequence of quote_eng \n\n quote_dup \n\n quote_vie
    # with quote_eng \n\n quote_vie
    text = re.sub(quote_eng + r'\n\n' + quote_dup, quote_eng, text)

    euler_vie = r"""
Leonhard Euler hiện thân cho tính thẩm mỹ của \emph{sự trôi chảy đại số không biên giới} (unbounded algebraic fluency). Đối với Euler, đại số không phải là 1 bộ công cụ tĩnh tại mà là 1 chất lưu sống động, dễ uốn nắn. Thiên tài của ông nằm ở khả năng thao tác với các biểu thức vô hạn, chuỗi phân kỳ, \& các hàm lượng giác bằng 1 sự tự tin giản dị, đầy tính vui đùa của 1 đứa trẻ xếp các khối hình. Trong việc giải Bài toán Basel ($\sum_{n=1}^\infty \frac{1}{n^2} = \frac{\pi^2}{6}$), ông đã cả gan coi chuỗi Taylor vô hạn của $\sin(x)/x$ như 1 đa thức hữu hạn, tiêu chuẩn với vô số nghiệm, phân tích nó thành 1 tích vô hạn.\footnote{Việc coi 1 đa thức vô hạn như 1 đa thức hữu hạn mà không thiết lập 1 cách nghiêm ngặt sự hội tụ đều hay áp dụng định lý phân tích Weierstrass là 1 cú nhảy vọt logic khổng lồ có thể khiến 1 sinh viên đại học hiện đại rớt môn Giải tích Thực (Real Analysis) ngay lập tức. Nhưng Euler sở hữu 1 trực giác vật lý phi thường về việc những thao tác hình thức nào là ``an toàn'' ngay cả khi các nền tảng nghiêm ngặt (thứ mà Cauchy \& Weierstrass sẽ không hình thức hóa cho đến cả thế kỷ sau) vẫn chưa được phát minh.} Tính thẩm mỹ của Euler là 1 động lượng vận hành thuần túy: viết ra 1 mối quan hệ hàm số, thao tác các ký hiệu của nó bằng 1 ngữ pháp số học táo bạo, không tì vết, \& chứng kiến các bất biến nền tảng tự lắp ráp lại với nhau trên trang giấy.
""".strip()

    euler_eng = r"Leonhard Euler embodied the aesthetic of \\emph\{unbounded algebraic fluency\}. To Euler, algebra was not a static toolset but a living, malleable fluid. His genius lay in his ability to treat infinite expressions, divergent series, and trigonometric functions with the casual, play-filled confidence of a child stacking blocks. In solving the Basel Problem \(\$\\sum_\{n=1\}\^\\infty \\frac\{1\}\{n\^2\} = \\frac\{\\pi\^2\}\{6\}\$\), he dared to treat the infinite Taylor series for \$\\sin\(x\)/x\$ as a standard, finite polynomial with an infinite number of roots, factoring it into an infinite product\.\\footnote\{.*?\} Euler's aesthetic was one of pure operational momentum: write down a functional relationship, manipulate its symbols with audacious, flawless arithmetic grammar, and watch the underlying invariants assemble themselves on the page\."

    # Find Euler eng and insert Euler vie after it.
    match = re.search(euler_eng, text, re.DOTALL)
    if match:
        inserted = match.group(0) + "\n\n" + euler_vie
        text = text[:match.start()] + inserted + text[match.end():]
    else:
        print("COULD NOT FIND EULER ENG")

    with open('NQBH_element_aestheticity.tex', 'w', encoding='utf-8') as f:
        f.write(text)

if __name__ == '__main__':
    fix_missing_translation()
