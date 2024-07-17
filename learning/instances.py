class Employee:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('Shawn', 'Adams', 50000)
emp_2 = Employee('Test', 'User', 60000)

#print(emp_1)
#print(emp_2)

print(emp_1.email)
print(emp_2.email)

# Prints the First and last name, but theres a better way to do this.
# print('{} {}'.format(emp_1.first, emp_1.last))
print(emp_1.fullname()) # better way

# These both do the same thing, but the top one doesnt have to pass in self. (emp_1)
print(emp_1.fullname()) # using instance
print(Employee.fullname(emp_1)) # using the class