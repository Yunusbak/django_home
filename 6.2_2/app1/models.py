from django.db import models

class person(models.Model):
    name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    age = models.IntegerField()

    class Meta:
        db_table = "person"

    def __str__(self):
        return f"{self.name} {self.last_name}"