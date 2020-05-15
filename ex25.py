number, count = 0, 0
while count != 5:
    while number % 7 == 0:
        for i in range(2, 7):
            if number % i != 1:
                count = 0
                continue
            else:
                count += 1
        if number % 7 == 0 and count == 5:
            break
        else:
            count = 0
            number += 1
    if count != 5:
        number += 1

print('Количество шаров минимум: ', number)
