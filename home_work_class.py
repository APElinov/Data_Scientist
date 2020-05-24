import math


class Fraction:

    def __init__(self, numerator, denominator=1):
        self.numerator = numerator
        self.denominator = denominator
        self.whole = self.numerator // self.denominator
        self.fractional = self.numerator % self.denominator
        self.nod = math.gcd(self.fractional, self.denominator)

    def __str__(self):
        if self.denominator > self.numerator:
            return '{}/{}'.format(self.fractional // self.nod, self.denominator // self.nod)
        else:
            return '{} целых и {}/{}'.format(self.whole, self.fractional // self.nod, self.denominator // self.nod)

    def __add__(self, other):
        numerator = self.numerator * other.denominator + self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __sub__(self, other):
        numerator = self.numerator * other.denominator - self.denominator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __mul__(self, other):
        numerator = self.numerator * other.numerator
        denominator = self.denominator * other.denominator
        return Fraction(numerator, denominator)

    def __truediv__(self, other):
        numerator = self.numerator * other.denominator
        denominator = self.denominator * other.numerator
        return Fraction(numerator, denominator)

    def __int__(self):
        return self.numerator // self.denominator

    def __float__(self):
        return self.numerator / self.denominator


class OperationsOnFraction(Fraction):

    def __init__(self, numerator, denominator):
        super().__init__(numerator, denominator)
        print(numerator)
        print(denominator)

    def getint(self):
        return self.numerator // self.denominator

    def getfloat(self):
        return self.numerator / self.denominator


fraction_1 = Fraction(342, 23)
fraction_2 = Fraction(34, 234)

addition = fraction_1 + fraction_2
subtraction = fraction_1 - fraction_2
multiplication = fraction_1 * fraction_2
division = fraction_1 / fraction_2

print('Сократили дроби и у нас: {} и {}'.format(fraction_1, fraction_2))
print('({}) + ({}) = {}'.format(fraction_1, fraction_2, addition))
print('({}) - ({}) = {}'.format(fraction_1, fraction_2, subtraction))
print('({}) * ({}) = {}'.format(fraction_1, fraction_2, multiplication))
print('({}) / ({}) = {}'.format(fraction_1, fraction_2, division))
print('int({}) = {}'.format(fraction_1, int(fraction_1)))
print('float({}) = {}'.format(fraction_1, float(fraction_1)))

print('getint({}) = {}'.format(fraction_1, OperationsOnFraction.getint(fraction_1)))
print('getfloat({}) = {}'.format(fraction_1, OperationsOnFraction.getfloat(fraction_1)))
