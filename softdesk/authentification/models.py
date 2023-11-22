from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    birthdate = models.DateField()
    can_be_contacted = models.BooleanField()
    can_data_be_shared = models.BooleanField()
