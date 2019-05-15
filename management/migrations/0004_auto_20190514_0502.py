# Generated by Django 2.1.7 on 2019-05-14 05:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0003_auto_20190509_1048'),
    ]

    operations = [
        migrations.CreateModel(
            name='DeptEmployee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_date', models.DateField()),
                ('to_date', models.DateField(null=True)),
                ('dept_no', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Departments')),
                ('emp_no', models.OneToOneField(on_delete=django.db.models.deletion.DO_NOTHING, to='management.Employee')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='deptemp',
            unique_together=set(),
        ),
        migrations.RemoveField(
            model_name='deptemp',
            name='dept_no',
        ),
        migrations.RemoveField(
            model_name='deptemp',
            name='emp_no',
        ),
        migrations.AlterField(
            model_name='deptmanager',
            name='dept_no',
            field=models.OneToOneField(db_column='dept_no', on_delete=django.db.models.deletion.DO_NOTHING, to='management.Departments'),
        ),
        migrations.AlterField(
            model_name='deptmanager',
            name='to_date',
            field=models.DateField(null=True),
        ),
        migrations.DeleteModel(
            name='DeptEmp',
        ),
        migrations.AlterUniqueTogether(
            name='deptemployee',
            unique_together={('emp_no', 'dept_no')},
        ),
    ]