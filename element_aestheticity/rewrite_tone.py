import re

with open("NQBH_element_aestheticity.tex", "r") as f:
    text = f.read()

# 1. Coffee & Marmalade
oe1 = r"There is a quiet, almost domestic grace in the way a drop of cold half-\&-half blooms inside hot coffee, unfolding in delicate, turbulent plumes that fluid dynamicists call \textit{Rayleigh--Taylor instability}, though to anyone in a sunlit kitchen at 7:00 in the morning, it is simply the 1st nice thing to happen all day."
ne1 = r"There is a grim, thermodynamic finality in the way a drop of cold half-\&-half detonates inside hot coffee. It unfolds in delicate, turbulent plumes of \textit{Rayleigh--Taylor instability} (a violent micro-collapse of entropy that, to a human observer at 7:00 in the morning, masquerades as domestic grace)."
text = text.replace(oe1, ne1)

oe1b = r"It exists in the strange overlap where pristine physical laws meet the sticky, asymmetric reality of daily life, where the same differential equations governing galactic rotation are also, with unbothered mechanical precision, calculating the exact parabolic splatter of a dropped jar of marmalade on kitchen linoleum."
ne1b = r"It thrives in the violent overlap where pristine formalism collides with sticky, asymmetrical reality; where the exact same tensor calculus governing the orbital decay of a dying star is currently, with unbothered, fatalistic precision, computing the maximum blast radius of a dropped jar of marmalade across kitchen linoleum."
text = text.replace(oe1b, ne1b)

ov1 = r"Tồn tại 1 nét duyên dáng tĩnh tại, gần như mang tính nội trợ, trong cái cách mà 1 giọt kem half-\&-half lạnh giá nở bung giữa lòng tách cà phê nóng hổi, cuộn trào thành những luồng chùm tinh tế \& nhiễu loạn mà các nhà động lực học chất lưu gọi là \textit{sự bất ổn định Rayleigh--Taylor}, mặc dù đối với bất kỳ ai đang đứng trong gian bếp ngập nắng vào lúc 7 giờ sáng, đó đơn thuần là điều tốt đẹp đầu tiên xảy đến trong ngày."
nv1 = r"Tồn tại một tính chung cuộc tàn khốc, mang đậm sắc thái nhiệt động lực học trong cái cách mà một giọt kem lạnh (half-\&-half) phát nổ giữa lòng tách cà phê nóng rẫy. Nó cuộn trào thành những luồng chùm tinh tế, nhiễu loạn của \textit{sự bất ổn định Rayleigh--Taylor} (một vi-sụp đổ bạo liệt của entropy mà đối với một kẻ quan sát nhân sinh vào lúc 7 giờ sáng, lại đội lốt một nét duyên dáng nội trợ)."
text = text.replace(ov1, nv1)

ov1b = r"Nó hiện hữu tại điểm giao thoa kỳ lạ, nơi các định luật vật lý nguyên sơ va chạm với thực tại nhầy nhụa \& bất đối xứng của đời sống thường nhật, nơi chính những phương trình vi phân chi phối chuyển động quay của dải thiên hà cũng đồng thời, với 1 sự chính xác cơ học lạnh lùng, tính toán ra quỹ đạo parabol văng vãi tuyệt đối của 1 hũ mứt cam vừa bị đánh rơi trên sàn bếp linoleum."
nv1b = r"Nó sinh sôi ở điểm giao thoa bạo lực nơi chủ nghĩa hình thức nguyên sơ va đập với thực tại nhầy nhụa, bất đối xứng; nơi mà chính phép tính tensor (tensor calculus) chi phối sự suy rã quỹ đạo của một ngôi sao đang hấp hối cũng đang đồng thời, với một sự chính xác lạnh lùng \& định mệnh, tính toán ra bán kính công phá cực đại của một hũ mứt cam vừa bị rơi vỡ trên sàn bếp linoleum."
text = text.replace(ov1b, nv1b)

# 2. Hamilton's Clumsiness
oe2a = r"In physics, Hamilton's Principle dictates that any dynamic system (whether a photon bending around a star or a dropped coffee mug plummeting toward the linoleum) will naturally traverse the specific path that minimizes the action integral:"
ne2a = r"In classical mechanics, Hamilton's Principle decrees that any dynamic system (whether a supermassive black hole devouring a photon or a tragically fumbled coffee mug plummeting toward its inevitable destruction on the linoleum) is bound by the exact same geometric fate. It will blindly and flawlessly traverse the singular trajectory that minimizes the action integral:"
text = text.replace(oe2a, ne2a)

oe2b = r"Nature is fundamentally stingy; it refuses to expend surplus energy."
ne2b = r"The universe is pathologically stingy; it refuses to subsidize surplus energy for our clumsiness."
text = text.replace(oe2b, ne2b)

ov2a = r"Trong vật lý, Nguyên lý Hamilton phán quyết rằng bất kỳ hệ động lực nào (cho dù là 1 hạt photon uốn cong quanh 1 ngôi sao hay 1 chiếc cốc cà phê bị đánh rơi đang lao cắm đầu xuống sàn linoleum) sẽ tự nhiên vạch ra 1 quỹ đạo cụ thể nhằm cực tiểu hóa tích phân tác dụng:"
nv2a = r"Trong cơ học cổ điển, Nguyên lý Hamilton phán truyền rằng bất kỳ hệ động lực nào (cho dù là một hố đen siêu khối lượng đang nuốt chửng một hạt photon hay một chiếc cốc cà phê bị tuột tay một cách bi thảm đang lao cắm đầu vào sự diệt vong tất yếu của nó trên sàn linoleum) cũng đều bị trói buộc bởi cùng một định mệnh hình học. Nó sẽ mù quáng \& hoàn mỹ băng qua một quỹ đạo duy nhất nhằm cực tiểu hóa tích phân tác dụng:"
text = text.replace(ov2a, nv2a)

ov2b = r"Tự nhiên về cơ bản là keo kiệt; nó từ chối tiêu tốn năng lượng thặng dư."
nv2b = r"Vũ trụ này mang một bản tính keo kiệt đến mức bệnh hoạn; nó dứt khoát khước từ việc trợ cấp năng lượng thặng dư cho sự vụng về của chúng ta."
text = text.replace(ov2b, nv2b)

# 3. Terminal Error Existential Dread
oe3 = r"You see it when staring at a terminal window at two in the morning, hunting down a structural error in an algorithmic model, only to discover a tragicomic data type conflict, a continuous cost expression stubbornly trying to inhabit an integer definition.\footnote{There is a specific, highly concentrated form of existential dread that accompanies debugging these kinds of data type conflicts. You spend hours questioning the fundamental logic of your continuous model, doubting the very theoretical bedrock of your mathematical formulation, only to realize the error is not philosophical, but typographical. The machine was not rejecting your logic; it was simply, rigidly pointing out that you cannot store a continuous floating-point cost expression inside a memory block explicitly declared as an integer. The resulting wave of relief, instantly followed by profound self-loathing, is arguably the most universal human experience in modern computational science."
ne3 = r"This aesthetic brutally manifests when staring into the void of a terminal window at two in the morning. You hunt down a perceived collapse in your mathematical architecture, only to uncover a profoundly humiliating data type conflict: a continuous cost expression stubbornly demanding asylum inside a discrete integer definition.\footnote{There is a highly toxic, concentrated form of existential dread reserved exclusively for this breed of debugging. You surrender hours to interrogating the metaphysical bedrock of your algorithmic model, convinced you have committed a grave offense against mathematics itself, only to discover the failure is not philosophical, but purely typographical. The compiler was never challenging your intellect; it was merely, with sociopathic indifference, pointing out that an infinite continuum of floating-point numbers cannot physically be shoved into an integer memory block. The subsequent wave of relief, instantly devoured by an abyss of self-loathing, is arguably the most unifying human experience in computational science."
text = text.replace(oe3, ne3)

ov3a = r"\textsf{Bản dịch:} Có 1 hình thái nỗi sợ hãi hiện sinh đặc thù, cô đặc cao độ đi kèm với việc gỡ lỗi (debugging) những kiểu xung đột kiểu dữ liệu như thế này. Bạn dành hàng giờ đồng hồ để chất vấn logic nền tảng của mô hình liên tục của mình, nghi ngờ chính cái lớp đá lý thuyết nền tảng trong công thức toán học của bạn, chỉ để nhận ra rằng lỗi lầm không mang tính triết học, mà mang tính đánh máy (typographical). Cỗ máy đã không hề bác bỏ logic của bạn; nó chỉ đơn giản, 1 cách cứng nhắc, chỉ ra rằng bạn không thể lưu trữ 1 biểu thức chi phí dấu phẩy động (floating-point) liên tục bên trong 1 khối bộ nhớ được khai báo hiển ngôn là 1 số nguyên. Làn sóng nhẹ nhõm theo sau đó, ngay lập tức được nối tiếp bởi 1 sự tự thù ghét bản thân sâu sắc, được cho là trải nghiệm mang tính con người phổ quát nhất trong khoa học điện toán hiện đại.}"
nv3a = r"\textsf{Bản dịch:} Có một hình thái nỗi sợ hãi hiện sinh độc hại, cô đặc cao độ được dành riêng cho chủng loại gỡ lỗi (debugging) này. Bạn cống hiến hàng giờ đồng hồ để tra khảo tầng đá gốc siêu hình của mô hình thuật toán của mình, đinh ninh rằng mình đã phạm phải một tội ác tày trời chống lại chính toán học, chỉ để phát hiện ra sự thất bại không hề mang tính triết học, mà hoàn toàn mang tính đánh máy. Trình biên dịch chưa từng bao giờ thách thức trí tuệ của bạn; nó chỉ đơn thuần, với một sự thờ ơ mang tính ái kỷ bệnh hoạn (sociopathic indifference), chỉ ra rằng một thể liên tục vô hạn của các số dấu phẩy động (floating-point) không thể nào bị nhét gượng ép về mặt vật lý vào một khối bộ nhớ số nguyên. Làn sóng nhẹ nhõm theo sau đó, ngay lập tức bị nuốt chửng bởi một vực thẳm của sự tự thù ghét bản thân, có lẽ là trải nghiệm mang tính nhân loại hợp nhất (unifying) nhất trong khoa học điện toán.}"
text = text.replace(ov3a, nv3a)

ov3b = r"Bạn nhìn thấy nó khi nhìn chằm chằm vào 1 cửa sổ dòng lệnh (terminal) lúc hai giờ sáng, săn lùng 1 lỗi cấu trúc trong 1 mô hình thuật toán, để rồi phát hiện ra 1 sự xung đột kiểu dữ liệu bi hài, 1 biểu thức chi phí liên tục đang bướng bỉnh cố gắng trú ngụ trong 1 định nghĩa số nguyên."
nv3b = r"Tính thẩm mỹ này biểu lộ một cách tàn bạo khi ta nhìn chằm chằm vào khoảng không hư vô của một cửa sổ dòng lệnh (terminal) lúc hai giờ sáng. Bạn săn lùng một sự sụp đổ được giả định trong kiến trúc toán học của mình, chỉ để phơi bày một sự xung đột kiểu dữ liệu nhục nhã sâu sắc: một biểu thức chi phí liên tục đang bướng bỉnh đòi tị nạn bên trong một định nghĩa số nguyên rời rạc."
text = text.replace(ov3b, nv3b)

with open("NQBH_element_aestheticity.tex", "w") as f:
    f.write(text)

print("Replacement successful")
