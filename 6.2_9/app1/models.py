from django.db import models

class nine(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()
