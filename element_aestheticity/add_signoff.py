with open("NQBH_element_aestheticity.tex", "r", encoding="utf-8") as f:
    text = f.read()

target = r"mang đậm tính người 1 cách ngoạn mục, không hồi kết."

signoff = r"""mang đậm tính người 1 cách ngoạn mục, không hồi kết.

\vspace{1cm}
\begin{center}
    * \quad * \quad *
\end{center}
\vspace{0.5cm}

\textsf{[H, 29, writer wannabe; embedded a little bit of E. B. White's writing style]:} My coffee has finally reached room temperature, completing its irreversible thermodynamic decay toward ambient equilibrium. I have spent over forty pages attempting to impose a rigorous architectural order on the aesthetic chaos of the universe, only to realize that the act of writing this essay is exactly the kind of tragically optimistic, mathematically hopeless behavior it was trying to critique. The marmalade is still on the floor. The universe remains profoundly unbothered. I suppose I should probably clean it up.

\textsf{[H, 29 tuổi, tập tành viết lách; pha trộn đôi chút văn phong của E. B. White]:} Tách cà phê của tôi rốt cuộc cũng đã hạ xuống nhiệt độ phòng, hoàn tất sự suy rã nhiệt động lực học bất khả nghịch của nó để hướng tới trạng thái cân bằng môi trường. Tôi đã tiêu tốn hơn bốn mươi trang giấy nỗ lực áp đặt một trật tự kiến trúc nghiêm ngặt lên sự hỗn mang thẩm mỹ của vũ trụ, chỉ để nhận ra rằng chính hành động viết bài luận này lại là cái kiểu hành vi lạc quan một cách bi kịch và vô vọng về mặt toán học mà nó đang cố gắng phê phán. Vệt mứt cam vẫn còn dính trên sàn. Vũ trụ vẫn tỏ ra sâu sắc không bận tâm. Tôi cho rằng có lẽ tôi nên đi dọn dẹp nó thì hơn.
"""

text = text.replace(target, signoff)

with open("NQBH_element_aestheticity.tex", "w", encoding="utf-8") as f:
    f.write(text)

