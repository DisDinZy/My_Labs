import re

text = "SplitThisStringByUpperCase"

promt = r"([a-z])([A-Z])"

reop = re.sub(promt, r"\1 \2", text)

print(reop)