import random

class Character:
    def __init__(self,name,**kwargs):
        self.name = name

        for key, value in kwargs.item():
            setattr(self,key,value) 

class Theif:
    sneaky = True
    def pickpocket(self):
        if self.sneaky:
            print("Called by {}".format(self))
            return bool(random.randit(0.1))
        return False

    def hide(self,light_level):
        return self.sneaky and light_level < 10

"""
class Theif:
    name = "Oliver"
    sneaky = True

    def __init__(self,name,sneaky=True,**kwargs):
        self.name = name
        self.sneaky = sneaky

        for key, value in kwargs.items():
            setattr(self,key,value)

    def pickpocket(self):
        if self.sneaky:
            print("Called by {}".format(self))
            return bool(random.randit(0.1))
        return False

    def hide(self,light_level):
        return self.sneaky and light_level < 10

class Student:
    name = "Your Name"
    
    def praise(self):
        return "You inspire me, {}".format(self.name)1
    
    def reassurance(self):
        return "Chin up, {}. You'll get it next time!".format(self.name)
    
    def feedback(self,grade):
        if grade > 50:
            return self.praise()
        return self.reassurance()



"""    
me = Student()
me.name
"""

class Employee:

    raise_amt = 1.04

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amt)


class Developer(Employee):
    raise_amt = 1.10

    def __init__(self, first, last, pay, prog_lang):
        super().__init__(first, last, pay)
        self.prog_lang = prog_lang


class Manager(Employee):

    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_emp(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_emp(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_emps(self):
        for emp in self.employees:
            print('-->', emp.fullname())


dev_1 = Developer('Corey', 'Schafer', 50000, 'Python')
dev_2 = Developer('Test', 'Employee', 60000, 'Java')

mgr_1 = Manager('Sue', 'Smith', 90000, [dev_1])

print(mgr_1.email)

mgr_1.add_emp(dev_2)
mgr_1.remove_emp(dev_2)

mgr_1.print_emps()