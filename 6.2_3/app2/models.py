from django.db import models

# Create your models here.
class Country(models.Model):
    country = models.CharField(max_length=255)
    population = models.IntegerField()


    class Meta:
        db_table = "Country"
