#Create class Currency (amount, unit). Overload the '==' operator to determine if 2 currencies are equal.

class Currency:
    def __init__(self, amount, unit):
        self.amount = amount
        self.unit = unit

    def __eq__(self, other):
        return self.amount == other.amount and self.unit == other.unit  
    
c1 = Currency(100, "USD")
c2 = Currency(100, "USD")
print(c1 == c2)