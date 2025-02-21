import datetime

x = datetime.datetime.now()
u = datetime.timedelta(days = 1)

o = x - u
p = x + u

k = o.strftime("%d")
ko = p.strftime("%d")
kop = x.strftime("%d")

print("Yesterday:", k, "Today:", kop, "Tomorrow:", ko)