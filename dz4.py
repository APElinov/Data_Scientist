#Напишите программу, которая запрашивает целое пятизначное число
# и выводит сумму его цифр.

#Формат ввода:
#11111

#Формат вывода:
#5

summa = 0

while True:
    number = input("Введите целое пятизначное число: ")
    if len(number) != 5 or not number.isdigit():
        print("Вы ввели НЕ целое или НЕ пятизначное число!")
    else:
        break

for smb in number:
    summa += int(smb)

print("Сумма цифр введенного числа:", summa)