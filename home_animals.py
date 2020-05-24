class Pet:
    """Домашнее животное"""
    legs = 4
    has_tail = True

    def inspect(self):
        print('Всего ног:', self.legs)
        print('Хвост присутствует -', 'да' if self.has_tail else 'нет')


class Cat(Pet):
    """Кошка - является домашним животным"""

    def sound(self):
        print('Мяу!')


class Dog(Pet):
    """Собака - является домашним животным"""

    def sound(self):
        print('Гав!')


class Hamster(Pet):
    """Хомячок - является домашним животным"""

    def sound(self):
        print('Ццццццц!')

print("Котик")
my_pet = Cat()
my_pet.inspect()
my_pet.sound()

print("Собачка")
my_pet = Dog()
my_pet.inspect()
my_pet.sound()

print("Хомячок")
my_pet = Hamster()
my_pet.inspect()
my_pet.sound()