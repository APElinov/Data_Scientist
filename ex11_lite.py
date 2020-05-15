massive = input("Введите чиcла через запятую: ").split(',')

max1 = massive[0]
for num in massive:
    if int(num) > int(max1):
        max1 = int(num)

print("Самое большое число здесь: ", max1)