import re

with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

# 1. Global Replacement of "Bản dịch:" in footnotes
text = text.replace(r"\textsf{Bản dịch:}", r"\textsf{[T, 35, exhausted translator]:} \textbf{Bản dịch \& Phản biện:}")

# 2. Injecting Debate Block 1 (After Marmalade)
marmalade_vi = r"tính toán ra bán kính công phá cực đại của một hũ mứt cam vừa bị rơi vỡ trên sàn bếp linoleum."
debate1 = r"""tính toán ra bán kính công phá cực đại của một hũ mứt cam vừa bị rơi vỡ trên sàn bếp linoleum.

\vspace{2mm}
\textsf{[T, 35, exhausted physicist \& underpaid translator]:} \textit{Hold on. Can we stop for a second? The tensor calculus governing orbital decay is absolutely NOT computing the splatter of your marmalade. One involves General Relativity; the other is a low-velocity, non-relativistic fluid dynamics nightmare involving viscosity and surface tension. They are entirely different sets of PDEs. You are sacrificing thermodynamic reality for a cheap poetic juxtaposition. And please don't get me started on the thermodynamic cost of having to translate this "domestic grace" nonsense into rigorous Hán-Việt.}

\textsf{[T, 35, nhà vật lý kiệt sức \& dịch giả bị trả lương bèo bọt]:} \textit{Khoan đã. Chúng ta dừng lại một giây được không? Phép tính tensor chi phối sự suy rã quỹ đạo hoàn toàn KHÔNG HỀ tính toán sự văng vãi của hũ mứt cam của cậu. Một cái liên quan đến Thuyết Tương đối Tổng quát; cái kia là một cơn ác mộng về động lực học chất lưu phi tương đối tính, vận tốc thấp, bao hàm cả độ nhớt và sức căng bề mặt. Chúng là những tập hợp PDE (phương trình vi phân đạo hàm riêng) hoàn toàn khác biệt. Cậu đang hy sinh thực tại nhiệt động lực học chỉ để đổi lấy một sự kề sát đầy tính thi ca rẻ tiền. Và làm ơn đừng bắt tôi phải phàn nàn về cái giá phải trả về mặt nhiệt động lực học khi phải còng lưng phiên dịch mớ bùng nhùng "duyên dáng nội trợ" này sang một thứ tiếng Hán-Việt nghiêm ngặt.}
\vspace{2mm}"""
text = text.replace(marmalade_vi, debate1)

# 3. Injecting Debate Block 2 (After Euler)
euler_vi = r"chứng kiến các bất biến nền tảng tự lắp ráp lại với nhau trên trang giấy."
debate2 = r"""chứng kiến các bất biến nền tảng tự lắp ráp lại với nhau trên trang giấy.

\vspace{2mm}
\textsf{[T, 35]:} \textit{Euler didn't just "watch invariants assemble themselves." He forced them to. Treating an infinite series like a finite polynomial without proving uniform convergence is not "operational momentum"—it's a reckless gamble. The man just got lucky that history proved his intuition right. If I tried that in a peer-reviewed paper today, Reviewer 2 would obliterate my career before lunch.}

\textsf{[T, 35]:} \textit{Euler không hề chỉ "chứng kiến các bất biến tự lắp ráp." Ông ta đã cưỡng ép chúng. Cái việc coi một chuỗi vô hạn như một đa thức hữu hạn mà không hề chứng minh sự hội tụ đều hoàn toàn không phải là "động lượng vận hành" — nó là một canh bạc vô trách nhiệm. Gã đàn ông này chỉ ăn may vì lịch sử đã chứng minh trực giác của ông ta là đúng. Nếu hôm nay tôi mà thử làm cái trò đó trong một bài báo khoa học, Phản biện 2 (Reviewer 2) sẽ hủy diệt sự nghiệp của tôi ngay trước giờ ăn trưa.}
\vspace{2mm}"""
text = text.replace(euler_vi, debate2)

# 4. Injecting Debate Block 3 (After Grothendieck)
grothendieck_vi = r"khiến những định lý từng 1 thời là bất khả thi (intractable) trông giống như những hệ quả hiển nhiên, tầm thường của 1 ngôi nhà hình học cao cấp hơn."
debate3 = r"""khiến những định lý từng 1 thời là bất khả thi (intractable) trông giống như những hệ quả hiển nhiên, tầm thường của 1 ngôi nhà hình học cao cấp hơn.

\vspace{2mm}
\textsf{[T, 35]:} \textit{Yes, and at what cost? Grothendieck's "oceanic submersion" requires reading 10,000 pages of Éléments de géométrie algébrique just to define what a point is. This is not beauty; this is cognitive totalitarianism. You are so mesmerized by his "rising sea" metaphor that you conveniently ignore the thousands of graduate students who drowned trying to swim in it.}

\textsf{[T, 35]:} \textit{Đúng vậy, và cái giá phải trả là gì? Cái "sự chìm ngập đại dương" của Grothendieck đòi hỏi người ta phải cày cuốc 10,000 trang tài liệu Éléments de géométrie algébrique chỉ để định nghĩa xem một điểm là cái quái gì. Đây không phải là vẻ đẹp; đây là chủ nghĩa toàn trị về mặt nhận thức. Cậu bị thôi miên bởi cái ẩn dụ "đại dương dâng trào" của ông ta đến mức cậu cố tình lờ đi hàng ngàn nghiên cứu sinh đã chết đuối khi cố gắng bơi trong đó.}
\vspace{2mm}"""
text = text.replace(grothendieck_vi, debate3)

# 5. Injecting Debate Block 4 (Final Signoff)
signoff_vi = r"Tôi cho rằng có lẽ tôi nên đi dọn dẹp nó thì hơn."
debate4 = r"""Tôi cho rằng có lẽ tôi nên đi dọn dẹp nó thì hơn.

\vspace{1cm}
\textsf{[T, 35, still exhausted]:} Good luck violating the Second Law of Thermodynamics with a damp paper towel, H. I'm going to sleep. This codebase is closed.

\textsf{[T, 35, vẫn đang kiệt sức]:} Chúc may mắn với việc vi phạm Định luật Hai Nhiệt động lực học bằng một tờ khăn giấy ẩm nhé, H. Tôi đi ngủ đây. Mã nguồn (codebase) này chính thức đóng lại."""
text = text.replace(signoff_vi, debate4)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

