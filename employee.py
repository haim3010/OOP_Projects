import datetime

class Employee:

    num_emps = 0
    reise = 1.04

    def __init__(self,first,last,pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first+'.'+last+'@company.com'
        
        Employee.num_emps+=1 
    
    def Fullname(self):
        return f'{self.first} {self.last}'

    def apply_raise(self):
        total_pay = float(self.pay * self.reise)
        return total_pay

    @classmethod
    def set_raise(cls,amount):
        cls.amount = amount
    
    @staticmethod
    def is_workday(day):
        if day.weekday() ==5 or day.weekday() == 6: # Monday = 0 , Sunday = 6
            return False
        else:
            return True

class Devops(Employee):
    reise = 1.08
    def __init__(self,first,last,pay,tools=[]):
        super().__init__(first,last,pay)
        self.tools = tools

class Manager(Employee):
    def __init__(self,first,last,pay,employees=[]):
        super().__init__(first,last,pay)
        self.employees = employees
    
    def add_emp(self,emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def rm_emp(self,emp):
        if emp in self.employees:
            self.employees.remove(emp)
    
    def meneger_emps(self):
        for emp in self.employees:
            print("--->",emp.Fullname())


emp1 = Employee('Hai','Mon',1000)
emp2 = Employee('Ben','Tov',30000)
date = datetime.date(2022,2,8)
dev1 = Devops('Hai','Mon',1000,["python","bash"])
dev2 = Devops('Ben','Tov',30000,["python","bash"])
manager1 = Manager('Silent','Mobius',50000 , [dev1])
#print(Employee.is_workday(date))
#print(Employee.set_raise(1.05))
#print(emp1.apply_raise())
#print(Employee.num_emps)
#print(emp1.__dict__) # {'first': 'Hai', 'last': 'Mon', 'pay': 1000, 'email': 'Hai.Mon@company.com'}
#print(dev1.tools[0])
manager1.add_emp(dev2)
#print(manager1.meneger_emps())

