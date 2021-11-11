
class PolynomialException(Exception):
    def __init__(self, message=""):
        Exception.__init__(self, message)


class BreakpointReachedException(PolynomialException):
    def __init__(self, message="Allowed number of iterations reached", allowed_operations=None):
        if allowed_operations is None:
            PolynomialException.__init__(self, message)
        else:
            PolynomialException.__init__(self, f'{message}: {allowed_operations}')


class NoRootException(PolynomialException):
    def __init__(self, message=""):
        PolynomialException.__init__(self, message)


class NotARootException(PolynomialException):
    def __init__(self, message=''):
        PolynomialException.__init__(self, message)
