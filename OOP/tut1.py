### class, object, constructor



class Employee:
    def __init__(self,fname,lname,salary): #constructor
        self.fname = fname
        self.lname = lname
        self.salary = salary
        pass
    

raghav = Employee('raghav','jain',44000)
jack = Employee('jack','din',44000)

#raghav.fname = "raghav"
#raghav.lname = "jain"
#raghav.salary = 44000

#jack.fname = "jack"
#jack.lname = "din"
#jack.salary = 44000

print(raghav.fname,jack.fname)

