walls = int(input('Сколько стен поклеили обоями? '))
time_on_the_first_wall = int(input('Сколько минут клеили первую стену? '))
count = 0

for i in range(walls):
    count += time_on_the_first_wall + (5 * i)

hours = (count + 60 - 1) // 60

print('На поклейку обоев потратили часов: ', hours)

