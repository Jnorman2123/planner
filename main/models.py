from django.db import models
from django.utils import timezone

# Create your models here.


class User(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Availability(models.Model):
    date_available = models.DateField(default='')
    start_time = models.TimeField(default='')
    end_time = models.TimeField(default='')
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date_created = models.DateTimeField(default=timezone.now)
