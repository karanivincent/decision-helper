from django.db import models
from django.urls import reverse


# Create your models here.
class Employee(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )

    emp_no = models.IntegerField(primary_key=True)
    birth_date = models.DateField()
    first_name = models.CharField(max_length=14)
    last_name = models.CharField(max_length=16)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    hire_date = models.DateField()

    class Meta:
        db_table = 'employees'
        ordering = ['hire_date']

    def __str__(self):
        return self.first_name + ' ' + self.last_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse("management:employee_detail", kwargs={"pk": self.pk})
    
    def fullname(self):
        return self.first_name + ' ' + self.last_name
    

class Departments(models.Model):
    dept_no = models.AutoField(primary_key=True, null=False)
    dept_name = models.CharField(unique=True, max_length=40)
 
    class Meta:
        db_table = 'departments'

    def __str__(self):
        return self.dept_name

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

    def get_absolute_url(self):
        return reverse('management:departments_detail', kwargs={'pk': self.pk})
    
class DeptEmp(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_no')
    dept_no = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, db_column='dept_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_emp'
        unique_together = (('emp_no', 'dept_no'),)


class DeptManager(models.Model):
    dept_no = models.ForeignKey(Departments, on_delete=models.DO_NOTHING, db_column='dept_no')
    emp_no = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_no')
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'dept_manager'
        unique_together = (('emp_no', 'dept_no'),)
        

class Salaries(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_no')
    salary = models.IntegerField()
    from_date = models.DateField()
    to_date = models.DateField()

    class Meta:
        db_table = 'salaries'
        unique_together = (('emp_no', 'from_date'),)


class Titles(models.Model):
    emp_no = models.ForeignKey(Employee, on_delete=models.DO_NOTHING, db_column='emp_no')
    title = models.CharField(max_length=50)
    from_date = models.DateField()
    to_date = models.DateField(blank=True, null=True)

    class Meta:
        db_table = 'titles'