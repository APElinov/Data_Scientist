q_time = int(input("Введите количество секунд: "))

h = q_time // 3600
mm = str(q_time // 60 - h * 60).ljust(2, '0')
ss = str(q_time % 3600 % 60).ljust(2, '0')

print(h, mm, ss, sep=":")

