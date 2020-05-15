number = int(input("Ширина? "))
count = 1
for i in range(1, number + 1):
    print(('{:^%d}' % number).format('*' * count))
    if i < number / 2:
        count += 2
    else:
        count -= 2
