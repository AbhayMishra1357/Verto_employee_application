from django.contrib import admin
from django.urls import path, include
from employees.views import employee_list


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('employees.urls')),
    path('', employee_list, name="employee_list"),  
]
