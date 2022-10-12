"""
   how class variables  differ from instance variables
"""
# Class created
class Student:

    raised_amount = 1.5                                     # class variable

    def __init__(self, firstname, lastname, salary):        # created arguments
        # self.argument = instance_variable                 # argument & instance do not have to be the same
        self.firstname = firstname                          # setting the instance variables to the arguments
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + '.' + lastname + '@py.com' # notice: newly set here, wasn't an argument

    def fullname(self):                                     # creating a method for instance variables
        return '{} {}'.format(self.firstname, self.lastname)

    def increase_pay(self):                                 # creating a method for class variable
        self.salary = int(self.salary * self.raised_amount) # an increase of 1.5 times


std_1 = Student('Jamey', 'Kim', 2000 )
std_2 = Student('Mimi', 'Stace', 2400)

'''
checks if the instance variables contain the attribute
in here they dont have the attribute themselves, 
but they are accessing from the class variable
'''
# print(instance.attribute)
print(std_2.raised_amount)
print(std_1.raised_amount)
print(Student.raised_amount)



