from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Account(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    balance = models.IntegerField(default=0)


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    message = models.TextField()
