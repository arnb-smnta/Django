from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User  # Add this import

# Create your models here.


class ChaiVariety(models.Model):
    chaitype_choice=[
        ('ml',"Masala"),
        ('pl','plain'),
        ('nm',"no milk")
    ]
    name=models.CharField(max_length=100)
    image=models.ImageField(upload_to='chais/')
    date_added=models.DateTimeField(default=timezone.now)
    type=models.CharField(max_length=2,choices=chaitype_choice)
    description=models.TextField(default='')
    
    def __str__(self):
        return self.name

#one to many


class review(models.model):
    chai=models.ForeignKey(ChaiVariety,on_delete=models.CASCADE,related_name="reviews")
    user=models.ForeignKey(User,on_delete=models.CASCADE,related_name="reviews")
    