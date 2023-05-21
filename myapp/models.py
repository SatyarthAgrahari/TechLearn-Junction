from django.db import models

# Create your models here.
class MyUser(models.Model):
    Firstname=models.CharField(max_length=50)
    Lastname=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50)
    Contact=models.CharField(max_length=12)
    Password=models.CharField(max_length=50)
    Date=models.DateField()

    def __str__(self) -> str:
        return self.Email


