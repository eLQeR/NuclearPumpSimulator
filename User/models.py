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

    @property
    def is_valid(self):
        return self.role in 'admin,engineer,operator'

