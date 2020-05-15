count, num = 0, 1
while num != 0:
    num = int(input('Введите число (для выхода "0"): '))
    if num % 2 == 0 and num != 0:
        count += 1
print('Вы ввели четных чисел: ', count)