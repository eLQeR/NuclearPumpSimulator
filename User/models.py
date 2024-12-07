from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    ROLE_CHOICES = [
        ('operator', 'Operator'),
        ('admin', 'Admin'),
        ('engineer', 'Engineer'),
        ('viewer', 'Viewer'),
    ]
    role = models.CharField(max_length=20, choices=ROLE_CHOICES, default='viewer')

    def is_operator(self):
        return self.role == 'operator'

    def is_admin(self):
        return self.role == 'admin'

    def is_engineer(self):
        return self.role == 'engineer'
