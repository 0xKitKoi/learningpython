class Citizen:
    """ template to make citizens """
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
    def full_name(self, first_name, last_name):
        return first_name + " " + last_name
    greeting = "For the glory of Python!"

#a = Citizen("first", "second")
#a.full_name("first", "last")
