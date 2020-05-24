from random import randint

from termcolor import cprint


class Man:

    def __init__(self, name):
        self.name = name
        self.fullness = 50
        self.house = None

    def __str__(self):
        return 'Я - {}, сытость {}%'.format(
            self.name, self.fullness)

    def eat(self):
        if self.house.food >= 10:
            cprint('{} поел'.format(self.name), color='yellow')
            self.fullness += 10
            self.house.food -= 10
        else:
            cprint('{} нет еды'.format(self.name), color='red')

    def work(self):
        cprint('{} сходил на работу'.format(self.name), color='blue')
        self.house.money += 50
        self.fullness -= 10

    def watch_MTV(self):
        cprint('{} смотрел MTV целый день'.format(self.name), color='green')
        self.fullness -= 10

    def shopping(self):
        if self.house.money >= 50:
            cprint('{} сходил в магазин за едой'.format(self.name), color='magenta')
            self.house.money -= 50
            self.house.food += 50
        else:
            cprint('{} деньги кончились!'.format(self.name), color='red')

    def go_into_the_house(self, house):
        self.house = house
        self.fullness -= 10
        cprint('{} въехал в дом!!!'.format(self.name), color='cyan')

    def act(self):
        if self.fullness <= 0:
            cprint('{} умер...'.format(self.name), color='red')
            return
        dice = randint(1, 6)
        if self.fullness < 20:
            self.eat()
        elif self.house.food < 10:
            self.shopping()
        elif self.house.money < 50:
            self.work()
        elif dice == 1:
            self.work()
        elif dice == 2:
            self.eat()
        else:
            self.watch_MTV()


class House:

    def __init__(self):
        self.food = 50
        self.money = 0

    def __str__(self):
        return 'В доме осталось {} дошираков, денег осталось {} рублей.'.format(
            self.food, self.money)


citizens = [
    Man(name='Бивис'),
    Man(name='Батхед'),
    Man(name='Кенни'),
]

my_sweet_house = House()
for citizen in citizens:
    citizen.go_into_the_house(house=my_sweet_house)

for day in range(1, 21):
    print('========== день {} =========='.format(day))
    for citizen in citizens:
        citizen.act()
    print('-------- в конце дня --------')
    for citizen in citizens:
        print(citizen)
    print(my_sweet_house)
