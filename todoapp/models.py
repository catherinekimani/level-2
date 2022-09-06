from django.db import models

# Create your models here.
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
    