from pyl.monomial import Monomial, Zero
from pyl.polynomial import Polynomial
from pyl.polynomialExceptions import NoRootException, BreakpointReachedException, NotARootException

__ACCURACY = 1e-14
__BREAKPOINT = 1e5
__DECIMAL_POINTS = 12


def derivative(arg):
    if isinstance(arg, Monomial):
        if arg.power == 0:
            return Zero()
        return Monomial(arg.factor * arg.power, arg.power - 1)
    elif isinstance(arg, Polynomial):
        li = [derivative(elem) for elem in arg.monomial_list if not elem.power == 0]
        return Polynomial(li)


def root(poly: Polynomial, start=complex(0.0, 0.0), accuracy=__ACCURACY, break_point=__BREAKPOINT,
         decimal_points=__DECIMAL_POINTS):
    if poly.is_const:
        raise NoRootException("Passed argument is a constant")
    der = derivative(poly)
    counter = 0
    complex_used = False
    x = start
    while abs(poly(x)) > accuracy:
        x -= poly(x)/der(x) if der(x) != 0 else poly(x)/der(x+1)
        counter += 1
        if counter * 2 > break_point and not complex_used:
            counter = 0
            x += (0 + 1j)
            complex_used = True
        if counter > break_point:
            raise BreakpointReachedException(allowed_operations=break_point)
    return complex(round(x.real, decimal_points), round(x.imag, decimal_points))


def horner(poli: Polynomial, val: complex, no_exception=False):
    degree = poli.monomial_list[0].power
    counter = 0
    table = []
    for i in range(degree+1):
        if poli.monomial_list[counter].power == degree - i:
            table.append(poli.monomial_list[counter].factor)
            counter += 1
        else:
            table.append(complex(0, 0))
    res = [complex(0, 0) for _ in table]
    res[0] = table[0]
    for i in range(1, len(table)):
        res[i] = val * res[i-1] + table[i]

    if no_exception:
        return Polynomial.from_factor_list(res[:-1])
    if res[-1] != 0:
        raise NotARootException(f'The value {val} is not a root of this polynomial')
    return Polynomial.from_factor_list(res[:-1])


