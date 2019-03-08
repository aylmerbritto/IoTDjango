from django.db import models
from django import forms

class realTimeModel(models.Model):
    temperature=models.CharField(max_length=250,null=True, blank=True)
    humidity=models.CharField(max_length=250,null=True, blank=True)
    pressure=models.CharField(max_length=250,null=True, blank=True)
    
    def approve(self):
        self.save()
        
    def __str__(self):
        List=[self.id,self.temperature,self.humidity,self.pressure]
        return str(List)
