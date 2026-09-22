with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

grothendieck_vi = r"khiến những định lý từng 1 thời bất trị nay trông giống như những hệ quả hiển nhiên, tầm thường xuất phát từ 1 mái nhà hình học bậc cao hơn."
debate3 = r"""khiến những định lý từng 1 thời bất trị nay trông giống như những hệ quả hiển nhiên, tầm thường xuất phát từ 1 mái nhà hình học bậc cao hơn.

\vspace{2mm}
\textsf{[T, 35]:} \textit{Yes, and at what cost? Grothendieck's "oceanic submersion" requires reading 10,000 pages of Éléments de géométrie algébrique just to define what a point is. This is not beauty; this is cognitive totalitarianism. You are so mesmerized by his "rising sea" metaphor that you conveniently ignore the thousands of graduate students who drowned trying to swim in it.}

\textsf{[T, 35]:} \textit{Đúng vậy, và cái giá phải trả là gì? Cái "sự chìm ngập đại dương" của Grothendieck đòi hỏi người ta phải cày cuốc 10.000 trang tài liệu Éléments de géométrie algébrique chỉ để định nghĩa xem một điểm là cái quái gì. Đây không phải là vẻ đẹp; đây là chủ nghĩa toàn trị về mặt nhận thức. Cậu bị thôi miên bởi cái ẩn dụ "đại dương dâng trào" của ông ta đến mức cậu cố tình lờ đi hàng ngàn nghiên cứu sinh đã chết đuối khi cố gắng bơi trong đó.}
\vspace{2mm}"""

text = text.replace(grothendieck_vi, debate3)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

print("Grothendieck fixed.")
