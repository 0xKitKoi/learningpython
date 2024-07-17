class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def show(self):
        print(F"I am {self.name} and I am {self.age} years old.")
        # F string. Read More About it.
    def speak(self):
        print("I don't know what to say.")

Min
class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age) #Super class is the init from Pet (Upper level parent class)
        self.color = color

    def speak(self):
        print("Meow")
# even though the cat class inherits the speak class from Pet, it will override it. same with dog.
    def show(self):
        print(F"I am {self.name} and I am {self.age} years old. And I am {self.color}")


class Dog(Pet):
    def speak(self):
        print("Bark")


class Fish(Pet):
    pass


p = Pet("Tim", 19)
# Notice the output.
p.show()
p.speak()
c = Cat("Bill", 34, "Brown")
c.show()
c.speak()
d = Dog("Jill", 25)
d.show()
d.speak()
f = Fish("Bubbles", 10)
f.speak()