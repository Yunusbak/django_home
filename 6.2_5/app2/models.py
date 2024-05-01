from django.db import models

# Create your models here.
class D(models.Model):
    name = models.CharField(max_length=255)
    num = models.IntegerField()
    
    class Meta:
        db_table = "D"

    def __str__(self) -> str:
        return f"{self.name} {self.num}"