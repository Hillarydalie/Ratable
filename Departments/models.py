from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class departments(models.Model):
    name = models.CharField(max_length=60)
    
    def __str__(self):
        return self.name

    def save_departments(self):
        self.save()

    def delete_departments(self):
        self.delete()    
    
