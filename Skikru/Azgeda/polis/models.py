from django.db import models


class Register(models.Model):
    name = models.CharField(max_length=50)
    phone = models.IntegerField()
    email = models.CharField(max_length=50)
    password = models.CharField(max_length=60)


# Create your models here.
