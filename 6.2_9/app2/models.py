from django.db import models

class nine_2(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()
