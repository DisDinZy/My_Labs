import re

text = "ConvertThisToSnakeCase"

promt = r"([a-z])([A-Z])"

reop = re.sub(promt, r"\1_\2", text)

reop = reop.lower()

print(reop)