from django.contrib import admin
from management.models import (Departments, Employee, 
                                Titles, Salaries,
                                DeptEmployee, DeptManager)

# Register your models here.
class DeptEmployeeAdmin(admin.ModelAdmin):
    list_display=['emp_no', 'dept_no']

class EmployeeAdmin(admin.ModelAdmin):
    list_display = ['fullname', 'gender']

class SalaryAdmin(admin.ModelAdmin):
    list_display = ['emp_no', 'amount']


admin.site.register(Departments)
admin.site.register(Employee, EmployeeAdmin)
admin.site.register(Salaries, SalaryAdmin)
admin.site.register(Titles)
admin.site.register(DeptEmployee, DeptEmployeeAdmin)
admin.site.register(DeptManager)