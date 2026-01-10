# Create a class Complex with private attributes real and imaginary parts. Overload '>=' operator to find the greatest number.

class Complex:
    def __init__(self, real, imag):
        self.__real = real
        self.__imag = imag

    def magnitude(self):
        return (self.__real**2 + self.__imag**2) ** 0.5

    def __ge__(self, other):
        return self.magnitude() >= other.magnitude()
    
c1 = Complex(3, 4)
c2 = Complex(1, 7)
print(c1.magnitude())
print(c2.magnitude())
print(c1 >= c2)