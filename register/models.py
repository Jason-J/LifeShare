from django.db import models

# Create your models here.

class Person(models.Model):
    p_id = models.IntegerField()
    name = models.CharField(max_length = 24,null= True)
    nickName = models.CharField(max_length = 36, null=True)
    email = models.CharField(max_length= 42, null= True)
    userPassword = models.CharField(max_length= 24)
    def __unicode__(self):
        return self.name