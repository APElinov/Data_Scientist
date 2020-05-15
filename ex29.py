numbers = int(input('Сколько граней у кубиков? '))

for i in range(1, numbers + 1):
    for k in range(1, numbers + 1):
        print('-'.join([str(i), str(k)]))