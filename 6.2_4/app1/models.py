from django.db import models

# Create your models here.
class A(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()


    class Meta:
        db_table = "A"