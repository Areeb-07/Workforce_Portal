from django.db import models

class Coordinator(models.Model):
    name=models.CharField(max_length=255,blank=True)
    roll_number=models.CharField(max_length=20)
    email=models.EmailField(blank=True)
    departments=models.CharField(max_length=255,blank=True)

class CG(models.Model):
    name=models.CharField(max_length=255)
    department=models.CharField(max_length=255,blank=True,null=True)
    email = models.EmailField(blank=True)

class Task(models.Model):
    task_id = models.CharField(max_length=30)
    task = models.CharField(max_length=255)
    sub_task = models.CharField(max_length=255)
    cg_email = models.EmailField()

class Progress(models.Model):
    task_number = models.CharField(max_length=30)
    task_id = models.CharField(max_length=30)
    progress = models.CharField(max_length=30)