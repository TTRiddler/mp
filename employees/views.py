from django.shortcuts import render, get_object_or_404
from django.views import View
from employees.models import Employee


class EmployeesView(View):
    def get(self, request):
        active_employees = Employee.objects.filter(is_active=True)
        leader = active_employees.filter(is_main=True).first()
        employees = active_employees.exclude(id=leader.id)

        context = {
            'employees': employees,
            'leader': leader
        }

        return render(request, 'employees/employees.html', context)
