### intance variable, class variables
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
        # self.salary = int(self.salary * self.increment) 
        self.salary = int(self.salary * Employee.increment) 

print(Employee.no_of_employees)    
   
mike = Employee('mike','bang',30000)
print(Employee.no_of_employees)

jay = Employee('jay','host',30000)
print(Employee.no_of_employees)
 

#print(mike.salary)
#mike.increase()
#print(mike.salary)

#print(mike.__dict__) ## printing all instance variable
#print(Employee.__dict__) ## printing all class variable