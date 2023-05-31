from django.db import models

# Create your models here.

class champ(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField(null=True)
    image = models.CharField(max_length=2000, null=True)