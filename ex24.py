number = int(input("Ширина? "))
for i in range(1, number + 1):
    # Центральная звезда
    if i == int(number / 2 + 1):
        print(('{:^%d}' % number).format('*'))
    else:
        # Верхняя половина креста
        if i <= int(number / 2):
            print(('{:^%d}' % number).format((' ' * (number - (i * 2))).join('*' * 2)))
        # Нижняя половина креста
        else:
            print(('{:^%d}' % number).format((' ' * ((i - (number - i)) - 2)).join('*' * 2)))
