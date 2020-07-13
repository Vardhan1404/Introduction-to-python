count = 0
sum = 0.0
while True:
    s = input("enter a number:")
    if s == 'done':
        break
    try:
        f = float(s)
    except:
        print('Invalid input')
        continue
    count = count + 1
    sum = sum + f
print(count,sum,sum/count)