from django.contrib import admin
from management.models import (Departments, Employee, 
                                Titles, Salaries)

# Register your models here.
admin.site.register(Departments)
admin.site.register(Employee)
admin.site.register(Salaries)
admin.site.register(Titles)