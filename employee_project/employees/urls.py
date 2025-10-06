from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet
from . import views as frontend_views

router = DefaultRouter()
router.register(r'employees', EmployeeViewSet, basename='employee')

urlpatterns = [
    path('api/', include(router.urls)),
    path('', frontend_views.employee_list, name='employee-list'),  # frontend route
    path("download_csv/", EmployeeViewSet.send_csv, name="download_csv"),
    path("send_mail/", EmployeeViewSet.send_email, name="send_mail"),
]
