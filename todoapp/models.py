from django.db import models

# Create your models here.
class Task(models.Model):
    name=models.TextField(max_length=250)
    priorit=models.IntegerField()
    date=models.DateField()

    def __str__(self):
        return self.name