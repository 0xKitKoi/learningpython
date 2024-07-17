class Dog:
    def __init__(self, name):
        self.name = name
        print(name)
    def bark(self):
        print("bark")

d = Dog("Tim")
d.bark()
print(type(d))