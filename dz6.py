# km_on_day = int(input("Сколько километров в день преодолевает машина?"))
# km_on_way = int(input("Какой длинной путь нужно преодолеть?"))
#
# not_full_day_on_way = km_on_way % km_on_day
#
# if not_full_day_on_way == 0:
#     days_on_way = km_on_way // km_on_day
# else:
#     days_on_way = km_on_way // km_on_day + 1
#
# print(days_on_way)

# km = 105
# dist = 120
# add = dist % km > 0
# day = dist // km + int(add)
# print(int(day))

km = 105
dist = 120
day = (dist + km - 1) // km
print(int(day))