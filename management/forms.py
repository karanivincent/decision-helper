from django.forms import ModelForm
from management.models import (Titles, Departments, Employee)

class DepartmentsForm(ModelForm):

    class Meta():
        model = Departments
        fields = ('dept_name')

class EmployeeForm(ModelForm):

    class Meta():
        model=Employee
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'hire_date')

        