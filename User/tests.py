from django.test import TestCase
from django.urls import reverse
from django.contrib.auth import get_user_model
from .models import User

class UserTest(TestCase):
    def setUp(self):
        self.user = User.objects.create(username='testuser', password='12345', role='admin')
        self.admin_user = get_user_model().objects.create_superuser(username='admin', password='adminpass')

    # Тести для моделі User
    def test_user_role(self):
        self.assertEqual(self.user.role, 'admin')
        self.assertTrue(self.user.is_admin())
        self.assertFalse(self.user.is_operator())
        self.assertFalse(self.user.is_engineer())

    # Тести для представлень
    def test_user_list_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('user_list'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_user_detail_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.get(reverse('user_detail', args=[self.user.pk]))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, 'testuser')

    def test_edit_user_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('edit_user', args=[self.user.id]), {
            'username': 'updateduser',
            'role': 'engineer'
        })
        self.assertEqual(response.status_code, 302)
        self.user.refresh_from_db()
        self.assertEqual(self.user.username, 'updateduser')
        self.assertEqual(self.user.role, 'engineer')

    def test_delete_user_view(self):
        self.client.login(username='admin', password='adminpass')
        response = self.client.post(reverse('delete_user', args=[self.user.id]))
        self.assertEqual(response.status_code, 302)
        self.assertFalse(User.objects.filter(username='testuser').exists())
