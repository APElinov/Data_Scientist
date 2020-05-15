first, second = '', ''
while True:
    num = int(input('Введите число (для выхода "0"): '))
    if first == '':
        first, second = num, num
    elif first == second:
        second = num
    elif num == 0:
        break
    elif num > first:
        first, second = num, first
    elif num > second:
        second = num

print('Второе по величине: ', second)
