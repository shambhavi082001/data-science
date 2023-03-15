### static method

class Employee:
    increment = 1.5 ## class variable
    no_of_employees = 0

    def __init__(self,fname,lname,salary):
        self.fname = fname ## instance variable
        self.lname = lname ## instance variable
        self.salary = salary ## instance variable
        self.increment = 1.3 ## instance variable
        Employee.no_of_employees +=1

    def increase(self):
        self.salary = int(self.salary * Employee.increment) 

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    @classmethod                ## alternative constructor               
    def from_str(cls, emp_string): 
        fname,lname,salary = emp_string.split("-")   
        return cls(fname,lname,salary) 

@staticmethod
def isopen(day):
    if day=="sunday":
        return False
    else:
        return True

print(Employee.isopen('sunday'))