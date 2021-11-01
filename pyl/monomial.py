
class Monomial:
    __EPSILON = 1e-15

    def __init__(self, factor=complex(1.0, 0), power=1):
        self.__power = power if power >= 0 else 1
        self.__factor = factor

    @property
    def power(self):
        return self.__power

    @property
    def factor(self):
        return self.__factor

    def __pow__(self, power):
        return Monomial(self.__factor, self.__power * power)

    def __str__(self):
        if self.__power == 0:
            return f'{self.__factor}'
        elif self.__power == 1:
            return f'{self.__factor}x'
        else:
            return f'{self.__factor}x^{self.__power}'

    def __call__(self, arg: complex) -> complex:
        return self.__factor * (arg ** self.__power)

    def __mul__(self, other):
        if isinstance(other, Monomial):
            return self.__mul_by_mono(other)
        else:
            return self.__mul_by_number(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul_by_number(self, number: complex):
        if number == complex(0.0, 0.0):
            return Zero()
        return Monomial(self.__factor * number, self.__power)

    def __mul_by_mono(self, monomial):
        return Monomial(self.__factor * monomial.__factor, self.__power + monomial.__power)

    def __add__(self, other):
        if isinstance(other, Monomial):
            return self.__add_mono(other)
        else:
            return self.__add_number(other)

    def __add_number(self, number):
        if complex(number) == complex(0.0, 0.0):
            return Monomial(self.__factor, self.__power)
        mono = Monomial(number, 0)
        from pyl.polynomial import Polynomial
        return Polynomial([self, mono])

    def __add_mono(self, mono):
        if self.__power == mono.power:
            if self.__factor + mono.factor <= self.__EPSILON:
                return Zero()
            return Monomial(self.__factor + mono.factor, self.__power)
        else:
            from pyl.polynomial import Polynomial
            return Polynomial([self, mono])


class Zero(Monomial):
    def __init__(self):
        Monomial.__init__(self, 0.0, 0)

    def __str__(self):
        return '0'


