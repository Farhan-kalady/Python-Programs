#Create a class Rectangle with private attributes length and width. Overload < operator to compute area of 2 rectangles.

class Rectangle:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def area(self):
        return self.__length * self.__width

    def __lt__(self, other):
        return self.area() < other.area()

r1 = Rectangle(4, 5)
r2 = Rectangle(3, 6)
if r1 < r2:
    print("Rectangle 1 has a smaller area than Rectangle 2")
else:
    print("Rectangle 1 has a larger area than Rectangle 2")
    
           