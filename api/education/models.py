from django.db import models


class Education(models.Model):
    university = models.CharField(max_length=250)
    city = models.CharField(max_length=250)
    country = models.CharField(max_length=250)
    title = models.CharField(max_length=250)
    start_date = models.DateField()
    end_date = models.CharField(max_length=13)
    description = models.TextField()
