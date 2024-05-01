from django.db import models

# Create your models here.
class Cars(models.Model):

    model = models.CharField(max_length = 255)

    make = models.CharField( max_length = 255, blank = True, null = True)

    year = models.IntegerField()

    price = models.IntegerField(blank=True, null=True)

    color = models.CharField(max_length = 255)

    class Meta:
        db_table = "cars"

    def __str__(self):
        return f"{self.model} {self.make}"
    
class Vehicle(models.Model):
    name = models.CharField(max_length=255)
    model = models.CharField(max_length=255)
    price = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = "vehicle"
    def __str__(self):
        return f"{self.name} {self.model}"