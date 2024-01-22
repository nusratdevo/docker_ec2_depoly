from django.db import models

# Create your models here.
class Position(models.Model):
    title = models.CharField(max_length=50)

    def __str__(self):
        return self.title

variation_choice = (
    ("Leader", "leader"),
    ("Manager", "manager"),
    ("Employee", "employee"),
)

class Employee(models.Model):
    fullname = models.CharField(max_length=100)
    emp_code = models.CharField(max_length=3)
    mobile= models.CharField(max_length=15)
    position = models.CharField(max_length=50, choices=variation_choice) 
