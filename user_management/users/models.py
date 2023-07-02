from django.db import models
from django.contrib.auth.models import AbstractUser


class Users(AbstractUser):
    ROLES = (
        ('student', 'Student'),
        ('staff', 'Staff'),
        ('admin', 'Admin'),
        ('editor', 'Editor'),
    )

    mobile = models.CharField(max_length=15)
    user_role = models.CharField(max_length=10, choices=ROLES)
    country = models.CharField(max_length=50)
    nationality = models.CharField(max_length=50)
    email = models.EmailField(unique=True)
    username = None
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    @property
    def full_name(self):
        return self.first_name + ' ' + self.last_name

    def __str__(self):
        return self.full_name
