from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import csv
from .models import Employee
from .serializers import EmployeeSerializer
from django.core.mail import send_mail
from django.conf import settings
from django.http import JsonResponse
from rest_framework import viewsets
from .models import Employee
from .serializers import EmployeeSerializer

class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer

def employee_list(request):
    return render(request, 'employees/employee_list.html')


class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all().order_by('-created_at')
    serializer_class = EmployeeSerializer

    @action(detail=False, methods=['get'])
    def send_csv(self, request):
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="employees.csv"'

        writer = csv.writer(response)
        # Add header row
        writer.writerow(['ID', 'Name', 'Email', 'Position', 'Department', 'Joining Date', 'Salary', 'Mobile Number', 'Created At'])

        employees = Employee.objects.all()
        for emp in employees:
            writer.writerow([
                emp.id,
                emp.name,
                emp.email,
                emp.position,
                emp.department,
                emp.joining_date,
                emp.salary,
                emp.mobile_number,
                emp.created_at,
            ])

        return response

    @action(detail=False, methods=['post'])
    def send_email(self, request):
        if request.method == "POST":
            subject = "Employee Report"
            employees = Employee.objects.all()
            
            message = "Employee Details:\n\n"
            for emp in employees:
                message += f"""
                Name: {emp.name}
                Email: {emp.email}
                Position: {emp.position}
                Department: {emp.department}
                Joining Date: {emp.joining_date}
                Salary: {emp.salary}
                Mobile: {emp.mobile_number}
                ----------------------------
                """

            send_mail(
                subject,
                message,
                settings.DEFAULT_FROM_EMAIL,
                ["recipient@example.com"],  # change to actual email
                fail_silently=False,
            )

            return JsonResponse({"status": "success", "message": "Mail sent successfully"})

