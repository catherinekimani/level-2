from django.db import models
from cloudinary.models import CloudinaryField
from django.contrib.auth.models import User
# Create your models here.
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    user_bio = models.TextField(max_length=150)
    user_contact = models.EmailField(max_length=100)
    user_profile = CloudinaryField('image')
    location = models.CharField(max_length=100,blank=True,null=True)
    
    def __str__(self):
        return f'{self.user} Profile'


class TodoList(models.Model):
    PRIORITY_CHOICES = (
        ('High','High'),
        ('Medium','Medium'),
        ('Low','Low'),
    )
    task_name = models.CharField(max_length=255)
    priority= models.CharField(choices=PRIORITY_CHOICES,max_length=100)
    
    
    def __str__(self):
        return self.task_name
    