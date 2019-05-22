from django.db import models
from django.core.validators import RegexValidator


class Post(models.Model):
    Name = models.CharField(max_length=20,null=True,blank=True)
    Department = models.TextField(choices=(("UI","UI"),("AWS","AWS"),("Newtworking","Newtworking"),("Human Resource","Human Resource"), ("Software Developer","Software Developer")),null=True,blank=True)
    Image = models.ImageField(upload_to='images/',null=True,blank=True)
    Gender=models.TextField(choices=(("Male","Male"),("Female","Female")),null=True,blank=True)
    Address=models.TextField(null=True,blank=True)
    Email=models.EmailField(null=True,blank=True)
    phone_regex = RegexValidator(regex=r'^\+?1?\d{9,15}$',
                                 message="Phone number must be entered in the format: '+919999999'. Up to 10 digits allowed.")
    Phone_number = models.CharField(validators=[phone_regex], max_length=10, blank=True,null=True)  # validators should be a list
    DateofJoining=models.DateField(null=True,blank=True)

    def __str__(self):
        return self.Name