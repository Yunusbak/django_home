from django.db import models

# Create your models here.
class ten_2(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()