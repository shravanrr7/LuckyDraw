from django.db import models

# Create your models here.
class lotteadm(models.Model):
	number=models.CharField(max_length=20)
	price=models.CharField(max_length=20)
