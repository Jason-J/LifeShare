from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Person(User):

    nickName = models.CharField(max_length = 36, null=True)


    def __unicode__(self):
        return self.name