from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class User(models.Model):
    first_name = models.CharField(max_length=30, null=True, blank=True)
    last_name = models.CharField(max_length=30, null=True, blank=True)
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #organisation = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.last_name
