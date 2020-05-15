number = int(input("Число? "))
amount = 0
for i in range(1, number + 1):
    amount += i ** 2
print('Сумма квадратов равна: ', amount)