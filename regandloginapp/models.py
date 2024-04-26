from django.db import models
class Reg(models.Model):
    firstname= models.CharField(max_length=20)
    lastname= models.CharField(max_length=20)
    email= models.EmailField()
    mobile=models.CharField(max_length=13)
    dob=models.CharField(max_length=10)
    username = models.CharField(max_length=10,primary_key=True)
    password= models.CharField(max_length=20)
    cpassword= models.CharField(max_length=20)





# Create your models here.
