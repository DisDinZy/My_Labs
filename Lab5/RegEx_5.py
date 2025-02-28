import re

text = ["acb", "a123b", "ab", "axxxxb", "bba", "abc"]

promt = r"^a.*b$"

reop = [ ]

for i in text:
    if re.fullmatch(promt, i):
        reop.append(i)

print(reop)