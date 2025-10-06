from django.db import models
from django.utils import timezone

class Employee(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    position = models.CharField(max_length=100)
    department = models.CharField(max_length=100)  # 👈 New field
    joining_date = models.DateField(default=timezone.now)  # 👈 New field
    salary = models.DecimalField(max_digits=10, decimal_places=2)  # 👈 New field
    mobile_number = models.CharField(max_length=15)  # 👈 New field
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name
