"""
    forming and action using the class and instances
    by ADDING METHODS to the class
    eg. want the full name of the student
"""

class Student:                                              # Class created
    def __init__(self, firstname, lastname, salary):        # created arguments
        # self.argument = instance_variable                 # argument & instance do not have to be the same
        self.firstname = firstname                          # setting the instance variables to the arguments
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + '.' + lastname + '@py.com' # notice: newly set here, wasn't an argument

    def fullname(self):                                     # creating a method
        return '{} {}'.format(self.firstname, self.lastname)

std_1 = Student('Jamey', 'Kim', 2000 )
std_2 = Student('Mimi', 'Stace', 2400)

print(std_1.fullname())
print(std_2.fullname())