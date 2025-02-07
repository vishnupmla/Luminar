# PayRoll Application
from abc import ABC, abstractmethod


class Employee(ABC):

    def __init__(self):
        self.empID = int(input('Enter the Employee ID: '))
        self.name = input('Enter the name: ')
        self.age = int(input('Enter the age: '))

    def show_details(self):
        print('\n---------Employee Details---------')
        print('Employee ID : ', self.empID)
        print('Employee Name : ', self.name)
        print('Age : ', self.age)

    @abstractmethod
    def calculate_salary(self):
        pass


class FixedSalary(Employee):
    def __init__(self):
        super().__init__()
        self.salary = int(input('Enter the salary per day: '))
        self.days = int(input('Enter the number of working days: '))

    def calculate_salary(self):
        self.monthly_salary = self.salary * self.days
        return self.monthly_salary

    def show_details(self):
        super().show_details()
        print('Monthly Salary = ', self.calculate_salary())


class Hourly_salary(Employee):

    def __init__(self):
        super().__init__()
        self.hours = int(input('Enter the total hours worked: '))
        self.rate = int(input('Enter the hourly payable amount: '))

    def calculate_salary(self):
        self.salary = self.hours * self.rate
        return self.salary

    def show_details(self):
        super().show_details()
        print('Total Hours worked : ', self.hours)
        print('Total Salary = ', self.calculate_salary())


lst = []
while 1:
    print('\nChoose from the menu\n1. Add Employees\n2. Monthly salary details\n3. Exit')
    ch = int(input('Enter the choice: '))

    if ch == 1:
        print('\nChoose the type of salary paid\n1. Monthly Salary\n2. Hourly Salary')
        type = int(input('\nEnter the choice: '))
        if type == 1:
            ob = FixedSalary()
            lst.append(ob)
        elif type == 2:
            ob = Hourly_salary()
            lst.append(ob)
        else:
            print('Enter a valid choice..!')

    elif ch == 2:
        emp_no = int(input('Enter the Employee ID: '))
        for i in lst:
            if i.empID == emp_no:
                i.show_details()
                break
            else:
                print('No employee found!!')

    elif ch == 3:
        print('Exiting...!')
        exit()

    else:
        print('Enter a valid choice')
