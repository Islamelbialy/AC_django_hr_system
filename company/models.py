from django.db import models

# Create your models here.
class Branches(models.Model):
    name = models.CharField(unique=True,null=False,max_length=50)
    address = models.CharField(null=True,max_length=50)
    email = models.EmailField(null=True,max_length=50,)

    def __str__(self):
        return self.name

class Departments(models.Model):
    name = models.CharField(max_length=50,null=False)
    phone = models.CharField(max_length=15,null=True)
    describtion = models.TextField(null=True)
    branche = models.ForeignKey(Branches,related_name='branche_dept',on_delete=models.CASCADE)

    def __str__(self):
        return self.name
