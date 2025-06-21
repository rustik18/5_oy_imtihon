from collections import namedtuple

Employee = namedtuple("Employee", ['name', 'hours_worked', 'rate'])
e1 = Employee("Rustamjon", 50, 1)
e2 = Employee("Bekzod", 25, 1)
e3 = Employee("Buldak", 45, 1)
def salary(employee):
    if employee.hours_worked > 40:
        rate_custom = 1.5
    else:
        rate_custom = 1
    return employee.hours_worked * rate_custom

print(salary(e1))