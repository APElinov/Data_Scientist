dictionary = []
while True:
    forward = input('!!!для выхода наберите "стоп"!!!\n'
                    '(ENTER - продолжить ввод) ')
    if forward != 'стоп':
        name = input('Введите имя: ').capitalize()
        gender = input('Введите пол (мужской/женский): ').lower()
        if gender == 'женский':
            age = int(input('Введите возраст: '))
            if 18 <= age <= 35:
                dictionary.append([name, [gender, age]])
                print('%s подходит как кандидат!' % name)
                print('-' * 30)
            else:
                print('%s не проходит как кандидат!' % name)
                print('-' * 30)
        else:
            print('%s не проходит как кандидат!' % name)
            print('-' * 30)
    else:
        break

print('Список кандидаток:')
for man in dictionary:
    print('-' * 30)
    print('Имя: ', dictionary[0][0])
    print('Пол: ', dictionary[0][1][0])
    print('Возраст: ', dictionary[0][1][1], 'лет.')
