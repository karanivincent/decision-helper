import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'decision_helper.settings')

import django
django.setup()


##fake Population script
import random
from management.models import Employee, Departments, DeptEmployee, Salaries

from faker import Faker

fakegen = Faker()

departments = ['Production', 'Research and Develpment', 'Purchasing', 'Marketing', 'Human Resource Management', 'Accounting and Finance']
gender = ['M', 'F']
salary = [50000, 30000, 100000, 60000, 80000]

def add_department():
    dep = Departments.objects.get_or_create(dept_name=random.choice(departments))[0]
    dep.save()
    return dep

def add_employee():
    sex = random.choice(gender)
    if sex == 'M':
        #employee fake data
        fake_fname = fakegen.first_name_male()
        fake_lname = fakegen.last_name_male()
        fake_dob = fakegen.date_between(start_date="-60y", end_date="-18y")
        fake_hdate = fakegen.date_between(start_date="-20y", end_date="-1y")
        employee = Employee.objects.get_or_create(birth_date=fake_dob, first_name=fake_fname, last_name=fake_lname, gender=sex, hire_date=fake_hdate)[0]
        
        
    else:
        fake_fname = fakegen.first_name_female()
        fake_lname = fakegen.last_name_female()
        fake_dob = fakegen.date_of_birth(tzinfo=None, minimum_age=18, maximum_age=60)
        fake_hdate = fakegen.date_between(start_date="-20y", end_date="-1y")
        employee = Employee.objects.get_or_create(birth_date=fake_dob, first_name=fake_fname, last_name=fake_lname, gender=sex, hire_date=fake_hdate)[0]
    
    return employee


def populate(N=5):
    for entry in range(N):
        #get random gender
        #get department for entry
        depart = add_department()
        employee = add_employee()

        #add Employee to departments
        depemployee = DeptEmployee.objects.get_or_create(emp_no=employee, dept_no=depart, from_date =fakegen.date_between(start_date="-10y", end_date="-1y"))[0]
        #add Salaries for employees
        salaryamount = random.choice(salary)
        salemployee = Salaries.objects.get_or_create(emp_no=employee, amount=salaryamount)[0]
         
if __name__== '__main__':
    print("populating script!")
    populate(30)
    print("populating complete!")



       
            