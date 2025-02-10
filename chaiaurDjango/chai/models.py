from django.db import models
from django.utils import timezone
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
    
    def __str__(self):
        return self.name

