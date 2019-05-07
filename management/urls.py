from django.urls import path
from management import views

app_name = 'management'

urlpatterns = [
    ######################################################################################################
    path('departments/', views.DepartmentsListView.as_view(), name='departments_list'),
    path('departments/new/', views.DepartmentsCreateView.as_view(), name='departments_new'),
    path('departments/detail/<int:pk>/', views.DepartmentsDetailView.as_view(), name='departments_detail'),
    path('departments/update/<int:pk>/', views.DepartmentsUpdateView.as_view(), name='departments_update'),
    path('departments/delete/<int:pk>/', views.DepartmentsDeleteView.as_view(), name='departments_delete'),
    ##############################################################################################################3
    path('employees/', views.EmployeeListView.as_view(), name='employee_list'),
    path('employee/new/', views.EmployeeCreateView.as_view(), name='employee_new'),
    path('employee/detail/<int:pk>/', views.EmployeeDetailView.as_view(), name='employee_detail'),
    path('employee/update/<int:pk>/', views.EmployeeUpdateView.as_view(), name='employee_update'),
    path('employee/delete/<int:pk>/', views.EmployeeDeleteView.as_view(), name='employee_delete'),
    
]
