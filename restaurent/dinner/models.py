from django.db import models

# Create your models here.
class menu(models.Model):
    Item=models.CharField(max_length=30)
    price=models.IntegerField()


    def __str__(self):
        return self.Item