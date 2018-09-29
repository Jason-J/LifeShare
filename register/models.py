from django.db import models

# Create your models here.

class Person(models.Model):
    p_id = models.IntegerField()
    name = models.CharField(max_length = 24)
    nickName = models.CharField(max_length = 36)
    email = models.CharField(max_length= 42)
    password = models.CharField(max_length= 24)
