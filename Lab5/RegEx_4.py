import re

text = "Hello World This is Python RegEx Test"

promt = r"[A-Z][a-z]+"

reop = re.findall(promt, text)

print(reop)