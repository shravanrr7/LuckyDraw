from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.deletion import CASCADE
from django.conf import settings

User = settings.AUTH_USER_MODEL


# Create your models here.
class nio(models.Model):
    amount = models.CharField(max_length=30)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    dat = models.DateField()
    tim=models.TimeField()

