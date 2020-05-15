num = int(input("Введите целое число больше 2: "))
count = 2

while num % count != 0:
    count += 1

print("Наименьший натуральный делитель:", count)

