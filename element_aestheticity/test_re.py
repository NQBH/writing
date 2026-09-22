import re
text = r"\part{The Aesthetics of Mathematical \& Logical Forms}"
part1_regex = r"(\\part\{The Aesthetics of Mathematical \\& Logical Forms\})"
print("Matched?", bool(re.search(part1_regex, text)))
