#Create a class Person with private attributes name and age. Compare 2 Persons by their age.

class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def campare_age(self, other):
        if self.__age > other.__age:
            return f"{self.__name} is older"
        elif self.__age < other.__age:
            return f"{other.__name } is older"
        else:
            return f"Same age"
        
age1 = Person("Farhan",25)
age2 = Person("Umesh",30)

print(age1.campare_age(age2))
                 