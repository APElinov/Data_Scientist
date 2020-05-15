number = int(input("Число? "))
amount, fc = 1, 0
for i in range(1, number + 1):
    amount *= i
    fc += amount
print('сумму 1! + 2! ... + n = :', fc)