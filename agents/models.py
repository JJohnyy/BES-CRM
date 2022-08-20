from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings

# Create your models here.

<<<<<<< HEAD
<<<<<<< HEAD
class User(models.Model):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
=======
=======
>>>>>>> parent of 4cd8c1d (deleted abstractuser)
class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=True)


class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
<<<<<<< HEAD
>>>>>>> parent of 4cd8c1d (deleted abstractuser)
=======
>>>>>>> parent of 4cd8c1d (deleted abstractuser)

    def __str__(self):
        return self.user.username


class Agent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #organisation = models.ForeignKey(User, on_delete=models.CASCADE)
   
    def __str__(self):
        return self.user.last_name
