from django.db import models

# Create your models here.
class Menu(models.Model):
    brand=models.CharField(max_length=20)
    flavour=models.CharField(max_length=30)
    quantity=models.IntegerField()
    price=models.IntegerField()

    def __str__(self):
        return self.brand
class note(models.Model):
    title=models.CharField(max_length=30)
    description=models.TextField(max_length=300)
   
    def __str__(self):
        return self.title
class contact(models.Model):
    name=models.CharField(max_length=20)
    number=models.IntegerField()

    def __str__(self):
        return self.name
