from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    pass


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    agent = models.ForeignKey('Agent', on_delete=models.CASCADE)

    def __str__(self):
        return self.last_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.last_name
