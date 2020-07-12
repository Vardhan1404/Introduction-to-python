def computepay(h,r):
    if h <= 40:
        pay= h*r
    elif h > 40:
        pay= 40*r +(h-40)*r*1.5
    return (pay)

hrs = input("Enter Hours:")
h = float(hrs)
rate = input("enter rate")
r = float(rate)
o = computepay(h,r)
print("Pay", o) 
