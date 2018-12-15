from __future__ import division
import math

class Rational(object):
    def __init__(self, numer, denom):
        if denom < 0:
            denom = (-denom)
            numer = (-numer)
        # Only reduce the fraction if both denom and numer are integers.
        if isinstance(denom, int)  and isinstance(numer, int):
            d = math.gcd(numer, denom)
            numer = int(numer / d)
            denom = int(denom / d)
        self.denom = denom
        self.numer = numer


    def __eq__(self, other):
        return self.numer == other.numer and self.denom == other.denom

    def __repr__(self):
        return '{}/{}'.format(self.numer, self.denom)

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom, self.denom * other.denom)

    def __sub__(self, other):
        return self + Rational((-other.numer), other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return self * other.invert()

    def __abs__(self):
        return Rational(abs(self.numer), abs(self.denom))

    def __pow__(self, power):
        if power == 0:
            return Rational(1,1)
        if power < 0:
            return self.invert() ** - power
        return Rational(pow(self.numer, power), pow(self.denom, power))

    def __rpow__(self, base):
        return pow(base, self.numer/self.denom)

    def invert(self):
        return Rational(self.denom, self.numer)
