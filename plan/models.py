from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    def __str__(self):
        return self.username
class Destination(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()

class Accommodation(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.CharField(max_length=50, default='700 $')

class UserReview(models.Model):
    destination = models.ForeignKey(Destination, on_delete=models.CASCADE)
    user = models.CharField(max_length=255)
    comment = models.TextField()
    rating = models.PositiveIntegerField()
