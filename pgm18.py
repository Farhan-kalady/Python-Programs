#Create class Engine (_power) and Wheels (_size). Derive the class Car (_model) from Engine & Wheels. Display details of the car using method overriding.

class Engine:
    def __init__(self, power):
        self.power = power
class Wheels:
    def __init__(self, size):
        self.size = size

class Car(Engine, Wheels):
    def __init__(self, model, power, size):
        super().__init__(power)
        Wheels.__init__(self, size)
        self.model = model

    def display(self):
        print(f"Car Model: {self.model}, Engine Power: {self.power}HP, Wheel Size: {self.size} inches")

car = Car("Sedan", 150, 16)
car.display()    