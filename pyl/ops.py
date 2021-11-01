from pyl.monomial import Monomial, Zero
from pyl.polynomial import Polynomial
from pyl.polynomialExceptions import NoRootException, BreakpointReachedException

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


