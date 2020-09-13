from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=128)
    entry = models.CharField(max_length=500)

    def __str__(self):
        return f"{self.name}: {self.user.first_name} {self.user.last_name}"
