#Create a class FruitBasket (fruit_name, price per kg). Overload '+' operator that adds two fruit baskets with unique fruits having least price from 2 baskets.

class FruitBasket:
    def __init__(self, fruit, price):
        self.fruit = fruit
        self.price = price

    def __add__(self, other):
        result = []

        if self.fruit == other.fruit:
            result.append((self.fruit, min(self.price, other.price)))
        else:
            result.append((self.fruit, self.price))
            result.append((other.fruit, other.price))

        return result

    def display(self):
        print(f"Fruit: {self.fruit}, Price per kg: {self.price}")


# Object creation must be outside class
b1 = FruitBasket("Apple", 150)
b2 = FruitBasket("Banana", 100)

b3 = b1 + b2

for fruit, price in b3:
    print(f"Fruit: {fruit}, Price per kg: {price}")


