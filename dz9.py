order = ['белое вино', 'салат Цезарь', 'паста Карбонара', 'чизкейк', 'шоколадный сорбет']

old = input("Что убрать из списка? ")
new = input("Что поставить взамен? ")
order[order.index(old)] = new
print(order)
