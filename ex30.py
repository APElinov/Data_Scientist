def print_all(**kwargs):
    for key, value in kwargs.items():
        print(value)

print_all(**{'1': 'яблоки', '2': 'молоко', '3': 'хлеб', '4': 'груши', '5': 'йогурт', '6': 'мясо'})