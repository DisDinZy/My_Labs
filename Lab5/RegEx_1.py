import re

pattern = r"a*b*"

text = ["a", "ab", "abb", "ac", "abc", "aabb"]

te = [ ]

for i in text:
    if re.fullmatch(pattern, i):
        te.append(i)
        
print(te)