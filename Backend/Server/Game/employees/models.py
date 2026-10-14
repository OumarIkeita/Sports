from django.db import models

# Create your models here.
class Employee(models.Model):
    emp_id = models.CharField(max_length=50, unique=True)
    emp_name = models.CharField(max_length=100)
    degination = models.CharField(max_length=100)

    def __str__(self):
        return (f"{self.emp_name} - {self.degination}")


class Social(models.Model):
    soc_name = models.CharField(max_length=100)
    soc_city = models.CharField(max_length=50)
    soc_phone = models.IntegerField( unique=True)

    def __str__(self):
        return self.soc_name