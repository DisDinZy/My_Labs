import re

text = "hello_world test_variable snake_case ExampleText"

promt = r"[a-z]+_[a-z]+"

fort = re.findall(promt, text)


print(fort)