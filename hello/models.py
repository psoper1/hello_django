from django.db import models

# Create your models here.

class champ(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000, null=True)
    splash = models.CharField(max_length=2000, null=True)
    lane = models.ForeignKey('Lane', on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']

class lane(models.Model):
    lane = models.CharField(max_length=100)

    def __str__(self):
        return self.lane