massive = []
i = 1
while i != '0':
    i = input("Вводите числа через enter, \nдля окончания ввода, нажмите 0\n==> ")
    if i.isnumeric():
        massive.append(int(i))

sorted_massive = []

num = sum(massive)
while len(sorted_massive) != len(massive):
    while massive.count(num) != 1:
        num -= 1
    else:
        sorted_massive.append(num)
        num -= 1

print("И второе по величине значение здесь: ", sorted_massive[1])
