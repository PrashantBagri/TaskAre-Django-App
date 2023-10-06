from django.db import models
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Task(models.Model):
#title, target date, isCompleted, description
    createdBy = models.CharField(max_length=100, blank=False, null=True)
    title = models.CharField(max_length=100)
    targetDate = models.DateField()
    isCompleted = models.BooleanField(default=False)
    description = models.CharField(max_length=500)
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

class newUser(AbstractUser):
    username = models.CharField(max_length=50, blank=False, unique=True)
    first_name=models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=100, blank=False)
    email = models.EmailField(max_length=50, blank=False, unique=True)
    category = models.TextField(null=True, blank=True)
    Task = models.ForeignKey(Task, on_delete=models.SET_NULL, null=True)
    

    USERNAME_FIELD = 'username'

    def __str__(self):
        return self.username
#email, username, firstname, category, completed, not completed, 