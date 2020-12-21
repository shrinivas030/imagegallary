from django.db import models

# Create your models here.
class gallarymodel(models.Model):
    imagetype=(
        ('Laptop','Laptop'),
        ('mobile','mobile'),
        ('accessories','accessories'),
        ('headphone','headphone'),
        ('light','light'))

    pic=models.ImageField(null=True,blank=True)
    catagory=models.CharField(choices=imagetype,max_length=50,default='Laptop')

    def __str__(self):
        return self.catagory