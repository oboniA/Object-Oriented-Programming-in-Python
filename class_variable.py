"""
   how class variables  differ from instance variables
"""
# Class created
class Student:
    no_of_students = 0                                      # class variable initiated
    raised_amount = 1.5                                     # class variable

    def __init__(self, firstname, lastname, salary):        # created arguments
        # self.argument = instance_variable                 # argument & instance do not have to be the same
        self.firstname = firstname                          # setting the instance variables to the arguments
        self.lastname = lastname
        self.salary = salary
        self.email = firstname + '.' + lastname + '@py.com' # notice: newly set here, wasn't an argument

        Student.no_of_students += 1

    def fullname(self):                                     # creating a method for instance variables
        return '{} {}'.format(self.firstname, self.lastname)

    def increase_pay(self):                                 # creating a method for class variable
        self.salary = int(self.salary * self.raised_amount) # an increase of 1.5 times


std_1 = Student('Jamey', 'Kim', 2000 )
std_2 = Student('Mimi', 'Stace', 2400)
print(Student.no_of_students)                               # if before the instances, will give 0


