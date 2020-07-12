hours = input("enter hours")
h = float(hours)
rate = input("enter rate")
try:
    r = float(rate)
except:
    quit()
if h <= 40:
    pay = h * r
elif h > 40:
    pay = 40 * r + (h-40)*r*1.5
print(pay)
