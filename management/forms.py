from django import forms
from management.models import Titles, Departments, Employee
from bootstrap_datepicker_plus import DatePickerInput

class DepartmentsForm(forms.ModelForm):

    class Meta():
        model = Departments
        fields = ('dept_name',)

class EmployeeForm(forms.ModelForm):

    class Meta():
        model=Employee
        fields = ('first_name', 'last_name', 'gender', 'birth_date', 'hire_date')
        widgets = {
            'birth_date':DatePickerInput(),
            'hire_date':DatePickerInput()
        }

        