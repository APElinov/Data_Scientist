data = [input("Клетка №%i: " %i).upper() for i in [1, 2]]
colors = ['ABCDEFGH'.index(i[0]) + int(i[1]) for i in data]
print("Ячейки одного цвета!") if colors[0] % 2 == colors[1] % 2 \
    else print("Ячейки разного цвета!")

