'''
    CLASS & INSTANCES
    * manually set up instance variable
    * automatically set up instane variable
'''
class Student:            # Class created
    pass

std_1 = Student()         # instance of the Class
std_2 = Student()


"""manually create instance variable"""

std_1.firstname = 'Jamey'
std_1.lastname = 'Kim'
std_1.email = 'jamey.kim@py.com'
std_1.salary = 2000

std_2.firstname = 'Mimi'
std_2.lastname = 'Stace'
std_2.email = 'stace.mimi@py.com'
std_2.salary = 2400

print(std_2.email)




