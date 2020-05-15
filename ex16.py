num = int(input("Введите число: "))
count = 0
for i in range(1, num + 1):
    if num % i == 0:
        count += 1

if count == 2:
    print("Это просто число!")
elif count == 1:
    print("Вы ввели единицу...")
else:
    print("Это составное число!")