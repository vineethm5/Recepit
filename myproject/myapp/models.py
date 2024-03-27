from django.db import models
class receipt(models.Model):
    itemname=models.CharField(max_length=100)
    quantity=models.CharField(max_length=100)
    price=models.CharField(max_length=100)
# Create your models here.
