numbers = []
i = 1
while i != '0':
    i = input("Вводите числа через enter, \nдля окончания ввода, нажмите 0\n==> ")
    if i.isnumeric():
        numbers.append(i)

# count = 0
# number = 0
#
# for num in numbers:
#     while count <= len(numbers):
#         if int(num) > int(numbers[count]):
#             count += 1
#
# print(numbers)



for num in numbers:
    ind = 0
    if int(num) >= int(numbers[ind]):
        number = num
        ind += 1

print('И самое большое значение здесь: ', number)
