numbers = []
i = 1
while i != '0':
    i = input("Вводите числа через enter, \nдля окончания ввода, нажмите 0\n==> ")
    if i.isnumeric():
        numbers.append(int(i))

max1, max2 = 0, 1

for i in numbers:
    if i > max1:
        max1, max2 = i, max1
    else:
        if i > max2:
            max2 = i

if max1 < max2:
    max1, max2 = max2, max1

print("И второе по величине значение здесь: ", max2)