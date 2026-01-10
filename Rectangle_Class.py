#Create Rectangle class with attributes length and breadth and methods to find area and perimeter. Compare two Rectangle objects by their area.

class Recatangle:
    def __init__(self, length, breadth):
        self.length = length
        self.breadth = breadth

    def area(self):
        return self.length * self.breadth

    def peremiter(self):
        return 2 * (self.length + self.breadth)
    
r1 = Recatangle(6, 4)
r2 = Recatangle(5, 3) 

print(f"Area of r1: {r1.area()}")
print(f"Area of r2: {r2.area()}")
print(f"Perimeter of r1: {r1.peremiter()}")
print(f"Perimeter of r2: {r2.peremiter()}")
print(f"R1 has larger area: {r1.area() > r2.area()}")
