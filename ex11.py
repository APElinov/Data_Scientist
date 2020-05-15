numbers = input("Введите чиcла через запятую: ").split(',')
for i in numbers:
    numbers[numbers.index(i)] = i.replace(' ', '')

while numbers.count('') > 0:
    numbers.remove('')

# for sim in numbers:
#     if sim.isalpha():
#         numbers.remove(numbers[int(numbers.index(sim))])

number = 0
ind = 0


for num in numbers:
    if num.isnumeric():
        if int(num) > int(numbers[ind]):
            number = num
            ind += 1
    else:
        numbers.remove(numbers[int(numbers.index(num))])


print(number)




