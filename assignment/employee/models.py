from django.db import models

# Create your models here.

class addEmployeeTable(models.Model):
    imageFile = models.ImageField(upload_to='images/', max_length=200)
    empName = models.CharField(max_length=60)
    empBirthDate = models.DateField()
    empEmail = models.EmailField()
    empNum = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.empName
