from django.db import models
from agents.models import Agent
# Create your models here.


class Lead(models.Model):
    first_name = models.CharField(max_length=20)
    last_name = models.CharField(max_length=20)
    age = models.IntegerField(default=0)
    address = models.CharField(max_length=100)
    phone = models.CharField(max_length=20)
    organisation = models.ForeignKey(Agent, on_delete=models.CASCADE)
    agent = models.ForeignKey(
        'agents.Agent', null=True, blank=True,
        on_delete=models.SET_NULL
    )
    category = models.ForeignKey(
        'Category', related_name="leads", null=True,
        blank=True, on_delete=models.SET_NULL
    )
    email = models.EmailField()
    description = models.TextField()

    def __str__(self):
        return self.last_name


class Category(models.Model):
    name = models.CharField(max_length=30)
    organisation = models.ForeignKey(Agent, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
