from django.db import models

# Create your models here.
class telephone(models.Model):
    model = models.CharField(max_length=255)
    make = models.CharField(max_length=255)
    year = models.IntegerField()

    class Meta:
        db_table = "telephone"

    def __str__(self):
        return f"{self.model} {self.year}"