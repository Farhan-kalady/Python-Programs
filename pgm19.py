#Create a class Person (name, age) with a constructor and a method display(). Create a class Employee (EmpID) from Person, override display() to include the ID. Create a derived class Faculty (department) from Employee, override display() to include the department. Create a separate class Researcher with a method can_do_research() that returns a string indicating the person can conduct research. Create a final class Professor which inherits from Faculty and Researcher.

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print(f"Name: {self.name}, Age: {self.age}")
class Employee(Person):
    def __init__(self, name, age, emp_id):
        super().__init__(name, age)
        self.emp_id = emp_id

    def display(self):
        super().display()
        print(f"Employee ID: {self.emp_id}")
class Faculty(Employee):
    def __init__(self, name, age, emp_id, department):
        super().__init__(name, age, emp_id)
        self.department = department

    def display(self):
        super().display()
        print(f"Department: {self.department}") 

class Researcher:
    def can_do_research(self):
        return "This person can conduct research."
class Professor(Faculty, Researcher):  
    def __init__(self, name, age, emp_id, department):
        Faculty.__init__(self, name, age, emp_id, department)

    def display(self):
        Faculty.display(self)
        print(self.can_do_research())
prof = Professor("Dr. Smith", 45, "E123", "Computer Science")
prof.display()              