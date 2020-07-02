from django.db import models

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)


class Availability(models.Model):
    date_available = models.DateField(default='')
    start_time = models.TimeField(default='')
    end_time = models.TimeField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    # date_created = models.DateTimeField
