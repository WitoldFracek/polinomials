
class Monomial:
    def __init__(self, symbol: str, factor=1.0, power=1):
        self.__power = power if power >= 0 else 1
        self.__symbol = symbol
        self.__factor = factor

    @property
    def symbol(self):
        return self.__symbol

    @property
    def power(self):
        return self.__power

    @property
    def factor(self):
        return self.__factor

    def __pow__(self, power):
        return Monomial(self.__symbol, self.__factor, self.__power * power)

    def __str__(self):
        if self.__power == 0:
            return f'{self.__factor}'
        elif self.__power == 1:
            return f'{self.__factor}{self.__symbol}'
        else:
            return f'{self.__factor}{self.__symbol}^{self.__power}'

    def __call__(self, arg: float):
        return self.__factor * (arg ** self.__power)

    def __mul__(self, other):
        if isinstance(other, Monomial):
            return self.__mul_by_mono(other)
        else:
            return self.__mul_by_number(other)

    def __rmul__(self, other):
        return self.__mul__(other)

    def __mul_by_number(self, number: float):
        return Monomial(self.__symbol, self.__factor * number, self.__power)

    def __mul_by_mono(self, monomial):
        return Monomial(self.__symbol, self.__factor * monomial.__factor, self.__power + monomial.__power)


class Zero(Monomial):
    def __init__(self, symbol: str):
        Monomial.__init__(self, symbol, 0.0, 0)


def derivative(mono: Monomial):
    if mono.power == 0:
        return Zero(mono.symbol)
    return Monomial(mono.symbol, mono.factor * mono.power, mono.power-1)

