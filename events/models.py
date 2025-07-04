from django.db import models
from django.utils import timezone
      
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50,blank=True)

    def __str__(self):
        return self.name


class Event(models.Model):
    
    STATUS_CHOICES= [
        ('draft','Draft'),
        ('published','Published'),
        ('canceled','Canceled'),
    ]
    
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    description = models.TextField()
    date = models.DateField()
    time = models.TimeField()
    location = models.CharField(max_length=200)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    participants = models.ManyToManyField('Participant',blank=True)
    
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='draft'
    )
    
    thumbnail = models.ImageField(
        upload_to='',
        blank=True,
        null=True
    )
    
    
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    
    
    
    def __str__(self):
        return self.name 
    
    
class Participant(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15,blank=True)
    
    def __str__(self):
        return self.name