from distutils.command.upload import upload
from django.db import models


class TrendyProducts(models.Model):
    name = models.CharField(max_length=255)
    price = models.FloatField()
    img = models.ImageField(upload_to='pics')
    offer = models.BooleanField(default=False)
    offeramt = models.FloatField()
# Create your models here.
