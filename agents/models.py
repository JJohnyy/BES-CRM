from django.db import models
from django.contrib.auth.models import User
from django.conf import settings

# Create your models here.

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    #email = models.EmailField(max_length=55)
    #username = models.CharField(max_length=20)
    #first_name = models.CharField(max_length=20)
    #last_name = models.CharField(max_length=20)

    def __str__(self):
        return self.user.last_name
