import math

class Rational:
    def __init__(self, numerator, denominator):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        gcd = math.gcd(numerator, denominator)
        self.numerator = numerator // gcd
        self.denominator = denominator // gcd
        if self.denominator < 0:
            self.numerator = -self.numerator
            self.denominator = -self.denominator

    def __str__(self):
        return f"{self.numerator}/{self.denominator}"

    def get_numerator(self):
        return self.numerator

    def get_denominator(self):
        return self.denominator

    def __add__(self, other):
        new_num = self.numerator * other.denominator + other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __sub__(self, other):
        new_num = self.numerator * other.denominator - other.numerator * self.denominator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __mul__(self, other):
        new_num = self.numerator * other.numerator
        new_den = self.denominator * other.denominator
        return Rational(new_num, new_den)

    def __eq__(self, other):
        return self.numerator == other.numerator and self.denominator == other.denominator

    def __lt__(self, other):
        return self.numerator * other.denominator < other.numerator * self.denominator

    def __gt__(self, other):
        return self.numerator * other.denominator > other.numerator * self.denominator

if __name__ == "__main__":
    r1 = Rational(1, 2)
    r2 = Rational(1, 3)
    print(f"r1: {r1}, r2: {r2}")
    print("Addition:", r1 + r2)
    print("Subtraction:", r1 - r2)
    print("Multiplication:", r1 * r2)
    print("Equality:", r1 == r2)
    print("Less than:", r1 < r2)
    print("Greater than:", r1 > r2)
