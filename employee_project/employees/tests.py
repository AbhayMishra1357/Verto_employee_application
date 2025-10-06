from django.test import TestCase
from django.urls import reverse
from django.core import mail
from rest_framework.test import APIClient
from rest_framework import status
from .models import Employee

class EmployeeAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        # Create initial employees
        self.e1 = Employee.objects.create(name="Alice", email="alice@example.com", position="Engineer")
        self.e2 = Employee.objects.create(name="Bob", email="bob@example.com", position="Manager")
        self.base = '/api/employees/'

    def test_list_employees(self):
        res = self.client.get(self.base)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(res.json()), 2)

    def test_create_employee(self):
        payload = {"name":"Charlie", "email":"charlie@example.com", "position":"Designer"}
        res = self.client.post(self.base, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        self.assertTrue(Employee.objects.filter(email='charlie@example.com').exists())

    def test_retrieve_employee(self):
        res = self.client.get(f"{self.base}{self.e1.id}/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.json()['email'], self.e1.email)

    def test_update_employee(self):
        payload = {"name":"Alice X","email":"alice@example.com","position":"Senior Engineer"}
        res = self.client.put(f"{self.base}{self.e1.id}/", payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.e1.refresh_from_db()
        self.assertEqual(self.e1.position, "Senior Engineer")

    def test_delete_employee(self):
        res = self.client.delete(f"{self.base}{self.e2.id}/")
        self.assertIn(res.status_code, (status.HTTP_204_NO_CONTENT, status.HTTP_200_OK))
        self.assertFalse(Employee.objects.filter(pk=self.e2.id).exists())

    def test_unique_email_validation(self):
        payload = {"name":"X","email":"alice@example.com","position":"X"}
        res = self.client.post(self.base, payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertIn('email', res.json())

    def test_csv_export(self):
        res = self.client.get(f"{self.base}csv/")
        self.assertEqual(res.status_code, 200)
        self.assertEqual(res['Content-Type'], 'text/csv')
        content = res.content.decode()
        self.assertIn('alice@example.com', content)

    def test_send_email(self):
        from django.conf import settings
        settings.EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'
        payload = {'employee_ids':[self.e1.id, self.e2.id], 'subject':'Hi', 'message':'Hello team'}
        res = self.client.post(f"{self.base}send_email/", payload, format='json')
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        # Check that emails were sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertIn('Hello team', mail.outbox[0].body)
        # recipients should include both
        self.assertEqual(set(mail.outbox[0].to), set([self.e1.email, self.e2.email]))
