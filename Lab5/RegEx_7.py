import re

text = "hello_world_example"

promt = r"_([a-z])"

reop = re.sub(promt, lambda m: m.group(1).upper(), text)

reop = reop[0].capitalize() + reop[1:]

print(reop)