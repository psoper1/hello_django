from django.db import models

# Create your models here.

class champ(models.Model):
    name = models.CharField(max_length=100)
    image = models.CharField(max_length=2000, null=True)
    splash = models.CharField(max_length=2000, null=True)
    # description = models.CharField(max_length=5000, null=True)
    # qTitle = models.CharField(max_length=100, null=True)
    # qDescription = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['name']