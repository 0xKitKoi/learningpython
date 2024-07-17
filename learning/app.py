class Person:
    number_of_people = 0
# Because number_of_people isnt defined in any method, and because it doesnt have access to an instance of a class,
# It is defined the entire class.

    def __init__(self, name):
        self.name = name


p1 = Person("Tim")
p2 = Person("Jill")

