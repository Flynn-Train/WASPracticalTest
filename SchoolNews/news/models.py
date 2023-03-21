from django.db import models

# Create your models here.


class News(models.Model):
    title = models.CharField(max_length=128)
    author = models.CharField(max_length=128)
    date = models.CharField(max_length=128)
    text = models.CharField(max_length=128)


    def __str__(self):
        return self.title