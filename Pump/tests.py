from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission
from .models import Pump

User = get_user_model()

class PumpTests(TestCase):

    def setUp(self):
        # Create test users
        self.admin_user = User.objects.create_user(username='admin', password='admin123')
        self.admin_user.user_permissions.add(Permission.objects.get(codename='add_pump'))
        self.admin_user.user_permissions.add(Permission.objects.get(codename='change_pump'))
        self.admin_user.user_permissions.add(Permission.objects.get(codename='delete_pump'))

        self.regular_user = User.objects.create_user(username='user', password='user123')

        # Create a test pump
        self.pump = Pump.objects.create(
            name="Test Pump",
            status="OFF",
            pressure=1.2,
            temperature=25.0,
            performance=10.5,
            power=3.7,
            rotation_speed=1500,
            is_wheel_rotating=False,
            valve_status="CLOSED",
        )

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_pump_list_view(self):
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_list'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_list.html')
        self.assertContains(response, "Test Pump")

    def test_pump_detail_view(self):
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_detail', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_detail.html')
        self.assertContains(response, "Test Pump")

    def test_pump_create_view_permission(self):
        # Test without login
        response = self.client.get(reverse('pump_create'))
        self.assertEqual(response.status_code, 403)

        # Test with regular user
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_create'))
        self.assertEqual(response.status_code, 403)

        # Test with admin user
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('pump_create'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_form.html')

    def test_pump_update_view_permission(self):
        # Test without login
        response = self.client.get(reverse('pump_update', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 403)

        # Test with regular user
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_update', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 403)

        # Test with admin user
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('pump_update', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_form.html')

    def test_pump_delete_view_permission(self):
        # Test without login
        response = self.client.get(reverse('pump_delete', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 403)

        # Test with regular user
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_delete', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 403)

        # Test with admin user
        self.client.login(username='admin', password='admin123')
        response = self.client.get(reverse('pump_delete', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_confirm_delete.html')

    def test_pump_control_view(self):
        self.client.login(username='user', password='user123')
        response = self.client.get(reverse('pump_control', args=[self.pump.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pump_control.html')
