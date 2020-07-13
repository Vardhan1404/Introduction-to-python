count = 0
largest = 0
for num in [2, 16, 98, 35, 65, 60]:
    count = count + 1
    largest = largest + num
    print(count, largest, num)
print('after', count, largest, largest / count)

