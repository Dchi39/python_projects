#define class
class Person:
    count = 0

    def __init__(self, name):
        self.full_name = name #Instance attribute
        Person.count += 1 #Increment the class attribute
        
    def introduce(self):
        #Instance method uses self to access the instance attribute 
        print(f"Hello, my name is {self.full_name}")

    @classmethod
    def population(cls):
        #Class method uses cls to access the class attribute
        print(f"Population: {cls.count}")

p1 = Person("John Doe")
p1.introduce() #Calling an intance method
p1.population() #Calling a class method

P2 = Person("dulitha chirath")
P2.introduce() #Calling an instance method
Person.population() #Calling a class method