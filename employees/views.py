from django.shortcuts import render, get_object_or_404
from django.views import View
from employees.models import Employee
from pages.models import Page


class EmployeesView(View):
    def get(self, request):
        active_employees = Employee.objects.filter(is_active=True)
        leader = active_employees.filter(is_main=True).first()
        employees = active_employees.exclude(id=leader.id)
        emp_page = Page.objects.filter(is_active=True, action='employees').first()

        context = {
            'employees': employees,
            'leader': leader,
            'emp_page': emp_page,
        }

        lo = '' if request.session.get('main_view') else 'lo/'
        return render(request, lo + 'employees/employees.html', context)
