'''
    CLASS & INSTANCES
    * manually set up instance variable
    * automatically set up instane variable
'''

"""Automatically create instance variable"""

class Student:  # Class created
    def __init__(self, firstname, lastname, salary):        # created arguments
        # self.argument = instance_variable                 # argument & instance do not have to be the same
        self.firstname = firstname                          # setting the instance variables to the arguments
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + '.' + lastname + '@py.com' # notice: newly set here, wasn't an arguement

std_1 = Student('Jamey', 'Kim', 2000 )
std_2 = Student('Mimi', 'Stace', 2400)

print(std_2.email)
