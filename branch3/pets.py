class Pet:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def talk(self):
        raise NotImplementedError("Subclass must impliment abstract method")

class Cat(Pet):
    def __init__(self, name, age):
        super().__init__(name, age) # You can run Super class methos like this
    def talk(self):
        return "Meow"

class Dog(Pet):
    def __init__(self, name, age):
        super().__init__(name, age)
    def talk(self):
        return "Woof"


def Main():
    #thePet = Pet("Pet", 1)
    #jess = Cat("Jess", 3)
    #print("Is jess a cat? " + str(isinstance(jess, Cat)))
    #print("Is Jess a Pet? " + str(isinstance(jess, Pet)))
    #print("Is the pet a cat? " + str(isinstance(thePet, Cat)))
    #print("Is the pet a pet? " + str(isinstance(thePet, Pet)))
    pets = [Cat("Jess", 3), Dog("Jack", 2), Cat("Fred", 5), Pet("thePet", 5)]
    for pet in pets:
        print("Name: " + pet.name + ", Age: " + str(pet.age) + ", says: " + pet.talk())



if __name__ == '__main__':
    Main()
        
