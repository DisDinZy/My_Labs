import re

text = ["a", "ab","abb","abbb","abbbb"]
promt = r"ab{2,3}"

fore = [ ]

for i in text:
    if re.fullmatch(promt, i):
        fore.append(i)
        
        
print(fore)