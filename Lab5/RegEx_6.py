import re

text = "Hello, world. Python is great!"

promt = r"[ ,\.]"

reop = re.sub(promt, ":", text)

print(reop)