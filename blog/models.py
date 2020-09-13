from django.db import models

# Create your models here.


class Blog(models.Model):
    author = models.CharField(max_length=64)
    title = models.CharField(max_length=128)
    abstract = models.CharField(max_length=300)
    content = models.CharField(max_length=10000)
    tags = models.CharField(max_length=1000, blank=True)

    def __str__(self):
        return f"{self.title}- {self.author}"
