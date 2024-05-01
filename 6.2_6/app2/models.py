from django.db import models

# Create your models here.
class home(models.Model):
    adres = models.CharField(max_length=255)
    price = models.IntegerField()
    

    class Meta:
        db_table = "home"

    def __str__(self) -> str:
        return f"{self.adres} {self.price}"

    