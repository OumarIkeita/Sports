from django.db import models

# Create your models here.
class Student_api(models.Model):
    id = models.AutoField(primary_key = True)
    student_id = models.CharField(max_length =50, unique=True)
    name = models.CharField(max_length = 100)
    branch = models.CharField(max_length = 100)

    def __str__(self):
        return self.name