# from django.contrib import admin
# from .models import Employee

# @admin.register(Employee)
# class EmployeeAdmin(admin.ModelAdmin):
#     list_display = ("id", "name", "email", "position")
#     search_fields = ("name", "email", "position")
from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "position", "department", "joining_date", "salary", "mobile_number", "created_at")
    search_fields = ("name", "email", "department")
