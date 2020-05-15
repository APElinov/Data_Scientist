letter = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
numbers = []
for i in range(1, 9):
    numbers.append([a + str(i) for a in letter])

cell_1 = input('Введите название первой ячейки: ').upper()
cell_2 = input('Введите название второй ячейки: ').upper()

color_1 = [(n, x.index(cell_1)) for n, x in enumerate(numbers) if cell_1 in x]
color_2 = [(n, x.index(cell_2)) for n, x in enumerate(numbers) if cell_2 in x]

if (color_1[0][0] + 1) % 2 != 0 and (color_1[0][1] + 1) % 2 != 0:
    color_1 = "черного"
else:
    color_1 = "белого"

if (color_2[0][0] + 1) % 2 == 0 and (color_2[0][1] + 1) % 2 == 0:
    color_2 = "черного"
else:
    color_2 = "белого"

if color_1 == color_2:
    print("Указанные ячейки обе %s цвета!" % color_1)
else:
    print("Ячейка %s %s цвета, а ячейка %s %s цвета." % (cell_1, color_1, cell_2, color_2))
