def proverka(number):
    return number % 7 == 0, number % 6 == 1, number % 5 == 1, \
           number % 4 == 1, number % 3 == 1, number % 2 == 1


count = 1
while not all(proverka(count)):
    count += 1

print(count)
