from django.db import models
from django.db.models.signals import pre_save
from src.utils import *
from django.contrib.auth.models import User

class TrainerRegistration(models.Model):
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    status  = models.BooleanField()

    def __str__(self):
        return self.user.first_name
# Create your models here.
