from django.db import models

# Create your models here.

class Student(models.Model):
    name = models.CharField(max_length=55)
    rollno = models.IntegerField(null=False, blank=False)
    Bio = models.TextField()
    division = models.CharField(max_length=1, default='A')
    def __str__(self):
        return self.name