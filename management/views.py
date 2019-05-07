from django.shortcuts import render
from management.models import (Departments, Employee)
from django.views.generic import (CreateView, DetailView,
                                 UpdateView, DeleteView,
                                  ListView )
from django.contrib.auth.mixins import LoginRequiredMixin
from management.forms import DepartmentsForm, EmployeeForm
from django.urls import reverse_lazy


# Create your views here.

class DepartmentsCreateView(LoginRequiredMixin, CreateView):
    model = Departments
    login_url = '/login/'
    # redirect_field_name = 'management/department_detail.html'
    form_class = DepartmentsForm

class DepartmentsDetailView(DetailView):
    model = Departments

class DepartmentsUpdateView(LoginRequiredMixin, UpdateView):
    model = Departments
    login_url = '/login/'
    form_class = DepartmentsForm

class DepartmentsDeleteView(LoginRequiredMixin, DeleteView):
    model = Departments
    success_url = reverse_lazy('departments_list')
