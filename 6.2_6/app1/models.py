from django.db import models

# Create your models here.
class planeta(models.Model):
    name = models.CharField(max_length=255)
    weight = models.IntegerField()

    class Meta:
        db_table = "planeta"

    