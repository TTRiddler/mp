from django.contrib import admin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'role', 'phone', 'email', 'is_active', 'image', 'image_tag')
        }),
    )

    list_display = ('name', 'role', 'phone', 'email', 'is_active')
    readonly_fields = ('image_tag',)
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('name', 'role', 'email')
