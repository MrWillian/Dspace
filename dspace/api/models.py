from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  country = models.CharField(max_length=50)
  state = models.CharField(max_length=40)
  city = models.CharField(max_length=50)
  place = models.CharField(max_length=60)
  latitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
  longitude = models.DecimalField(max_digits=22, decimal_places=16, blank=True, null=True)
