from django.urls import path
from employees import views


urlpatterns = [
    path('', views.EmployeesView.as_view(), name='employees'),
]