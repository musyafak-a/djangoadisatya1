from django.db import models

# Create your models here.
class student(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    created_time = models.DateTimeField(auto_now=True)
    number_student = models.IntegerField(max_length=10,null=True)

    def __str__(self):
        return self.name