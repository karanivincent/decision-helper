# Generated by Django 2.1.7 on 2019-05-09 10:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_auto_20190507_1538'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='salaries',
            name='salary',
        ),
        migrations.AddField(
            model_name='salaries',
            name='advance',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='salaries',
            name='amount',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='employee',
            name='emp_no',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='salaries',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='salary', to='management.Employee'),
        ),
        migrations.AlterField(
            model_name='titles',
            name='emp_no',
            field=models.ForeignKey(db_column='emp_no', on_delete=django.db.models.deletion.DO_NOTHING, related_name='title', to='management.Employee'),
        ),
    ]