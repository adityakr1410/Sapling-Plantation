from django.db import models

# Create your models here.

class projectManager(models.Model):
    def __str__(self):
        return self.name
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)



class projects(models.Model):
    def __str__(self):
        return str(self.id)
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)
    long=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)

class plants(models.Model):
    
    id=models.IntegerField(primary_key=True)
    p_id=models.IntegerField()
    a_id=models.IntegerField()
    name=models.CharField(max_length=60)
    type=models.CharField(max_length=60)
    long=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)
    datePlanted=models.CharField(max_length=60)
    lastChecked=models.CharField(max_length=60)
    status=models.CharField(max_length=60)
    about=models.CharField(max_length=60)