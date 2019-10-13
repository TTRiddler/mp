from django.contrib import admin
from employees.models import Employee


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('name', 'role', 'phone', 'email', 'is_active', 'is_main', 'image', 'image_tag')
        }),
    )

    list_display = ('name', 'role', 'phone', 'email', 'is_active', 'is_main')
    readonly_fields = ('image_tag',)
    list_editable = ('is_active', 'is_main')
    list_filter = ('is_active', 'is_main')
    search_fields = ('name', 'role', 'email')
