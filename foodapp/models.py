# models.py

from django.db import models

class Food(models.Model):

    food_id = models.CharField(max_length=70,blank=False,default='',primary_key=True)
    food_name = models.CharField(max_length=150, blank=False,default='')
    location = models.CharField(max_length=150, blank=False,default='')
    items = models.CharField(max_length=1024, blank=False,default='')
    lat_long = models.CharField(max_length=150, blank=False,default='')
    full_details = models.CharField(max_length=150, blank=False,default='')
