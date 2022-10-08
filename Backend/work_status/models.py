from django.db import models

class Coordinator(models.Model):
    name=models.CharField(max_length=255,blank=True)
    roll_number=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    departments=models.CharField(max_length=255,blank=True)
    current_task=models.CharField(max_length=255,blank=True)
    cg=models.CharField(max_length=255,blank=True)
    progress=models.CharField(max_length=20,blank=True)

class CG(models.Model):
    name=models.CharField(max_length=255)
    departments=models.CharField(max_length=255)