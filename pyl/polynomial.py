from pyl.monomial import Monomial, Zero


class Polynomial:
    def __init__(self, mono_list=None):
        if mono_list is None:
            self.__poly = []
        else:
            self.__poly = mono_list

    @property
    def monomial_list(self):
        return self.__poly

    def __add__(self, other):
        if isinstance(other, Monomial):
            return self.__add_mono(other)
        elif isinstance(other, Polynomial):
            return self.__add_poly(other)
        else:
            m = Monomial(other, 0)
            li = [elem for elem in self.__poly]
            li.append(m)
            return Polynomial(li)

    def __radd__(self, other):
        return self.__add__(other)

    def __add_mono(self, mono: Monomial):
        li = [elem for elem in self.__poly]
        appended = False
        for no, elem in enumerate(li):
            if elem.power == mono.power:
                li[no] = self.__poly[no] + mono
                appended = True
                break
        if not appended:
            li.append(mono)
        pl = Polynomial(li)
        pl.__normalise_list()
        return pl

    def __add_poly(self, poly):
        li = []
        i = 0
        j = 0
        while i < len(self.__poly) and j < len(poly.monomial_list):
            if self.__poly[i].power > poly.monomial_list[j].power:
                li.append(self.__poly[i])
                i += 1
            elif self.__poly[i].power == poly.monomial_list[j].power:
                li.append(self.__poly[i] + poly.monomial_list[j])
                j += 1
                i += 1
            else:
                li.append(poly.monomial_list[j])
                j += 1
        return Polynomial(li)

    def __normalise_list(self):
        self.__poly.sort(key=lambda elem: elem.power, reverse=True)
        self.__poly = [mono for mono in self.__poly if isinstance(mono, Monomial)]

    def __str__(self):
        ret = ''
        if not self.__poly:
            return str(Zero())
        for elem in self.__poly:
            ret += str(elem)
            ret += ' + '
        return ret[:-3]

    def __call__(self, arg):
        ret = 0
        for elem in self.__poly:
            ret += elem(arg)
        return ret

    @property
    def is_linear(self):
        return 1 <= len(self.__poly) <= 2 and self.__poly[0].power == 1

    @property
    def is_const(self):
        return not self.__poly or self.__poly[0].power == 0


