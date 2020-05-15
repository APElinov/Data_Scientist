year = int(input("Введите год: "))
if year % 100 == 0 and year % 400 != 0 or year % 4 != 0:
    print("В этом году 365 дней")
else:
    print("Это високосный год, в нем 366 дней! ")
