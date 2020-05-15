distance = int(input("Дистанция в км.? "))
run_in_day = int(input("Пробежали в первый день км.? "))
progress = int(input("Прогресс в % в день? "))
count = 1

while distance > run_in_day:
    run_in_day += run_in_day / 100 * progress
    count += 1

print("На подготовку уйдет %d дней" % count)
