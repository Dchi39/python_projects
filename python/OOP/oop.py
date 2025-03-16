#define class
class Person:
    def __init__(self, first_name, last_name):
        self.fa = first_name
        self.la = last_name
        self.full_name = f"{self.fa} {self.la}"

    def introduce(self):
        print(f"Hello, my name is {self.full_name}")

    @classmethod
    def help(cls):
        print("This is a Person class")

#Create object
p = Person("John", "Doe")

p.introduce()
p.help()

#Access attribute
print(f"First name: {p.fa}")
print(f"Last name: {p.la}")
print(f"Full name: {p.full_name}")