

class Monomial:
    def __init__(self, symbol: str, factor=1, power=1):
        self.__symbol = symbol
        self.__factor = factor
        self.__power = power if power >= 0 else 1

    def __pow__(self, power):
        return Monomial(self.__symbol, self.__factor, self.__power * power)

    def __str__(self):
        return f'{self.__factor}{self.__symbol}^{self.__power}'



