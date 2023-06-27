from django.db import models

# Create your models here.
class Job(models.Model):
    company = models.CharField(max_length=200)
    position = models.CharField(max_length=200)
    location = models.CharField(max_length=200,blank=True)
    date_applied = models.CharField(max_length=200,blank=True)
    status = models.CharField(max_length=200,blank=True)
    platform = models.CharField(max_length=200,blank=True)
    description = models.TextField(blank=True)
    link = models.TextField(blank=True)
    
    def __str__(self):
        return self.company + " - " + self.position