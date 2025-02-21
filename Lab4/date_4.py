import datetime
import math
import random

x = datetime.datetime.now()

#сегоднешняя дата
y = x.strftime("%d")

#любая дата
z = random.randint(1, 31)

print("Random date -", z)
print("Today -", y)

c = abs(int(y) - z)

print("Difference in seconds -", c * 24 * 60 * 60)