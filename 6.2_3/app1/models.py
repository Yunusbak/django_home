from django.db import models

# Create your models here.

class program_language(models.Model):
    name = models.CharField(max_length=255)
    year = models.IntegerField()
    version = models.IntegerField()


    class Meta:
        db_table = "program language"

    def __str__(self):
        return f"{self.name} {self.version}"
    