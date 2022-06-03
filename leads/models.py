from django.db import models
from django.db.models.signals import post_save
from django.contrib.auth.models import AbstractUser

# Create your models here.

class User(AbstractUser):
    is_organiser = models.BooleanField(default=True)
    is_agent = models.BooleanField(default=False)
    

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.username


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    agent = models.ForeignKey('Agent', null=True, blank=True, on_delete=models.SET_NULL)
    category = models.ForeignKey('Category', related_name="Leads", null=True, blank=True, on_delete=models.SET_NULL)
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.last_name


class Agent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.user.last_name


class Category(models.Model):
    name= models.CharField(max_length=30)
    organisation = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


def post_user_created_signal(sender, instance, created, **kwargs):
    if created:
        UserProfile.objects.create(user=instance)


post_save.connect(post_user_created_signal, sender=User)
