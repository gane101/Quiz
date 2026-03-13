from django.db import models

# Create your models here.


class Time(models.Model):
  time = models.IntegerField(max_length=255)
  name = models.CharField(max_length=255)
