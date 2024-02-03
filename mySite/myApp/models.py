from django.db import models

# Create your models here.

class projectManager(models.Model):
    def __str__(self):
        return self.name
    id=models.IntegerField(primary_key=True)
    name=models.CharField(max_length=60)

class projects(models.Model):
    def __str__(self):
        return str(self.name)
    projectId=models.IntegerField(primary_key=True)
    projectManagerId=models.ForeignKey(projectManager,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=60)
    long=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)
    state=models.CharField(max_length=30,default="od")
    region=models.CharField(max_length=30,default="bbs")

class areas(models.Model):
    def __str__(self):
        return self.name
    
    areaId=models.IntegerField(primary_key=True)
    projectManagerId=models.ForeignKey(projectManager,on_delete=models.CASCADE,default=1)
    projectId=models.ForeignKey(projects,on_delete=models.CASCADE,default=1)
    name=models.CharField(max_length=60)
    long=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)

class plants(models.Model):

    def __str__(self):
         return str(f"{self.plantId}-{self.areaId}-{self.projectId}")

    plantId=models.IntegerField(primary_key=True)
    projectManagerId=models.ForeignKey(projectManager,on_delete=models.CASCADE,default=1)
    projectId=models.ForeignKey(projects,on_delete=models.CASCADE,default=1)
    areaId = models.ForeignKey(areas,on_delete=models.CASCADE,default=1)

    name=models.CharField(max_length=60)
    type=models.CharField(max_length=60)
    long=models.CharField(max_length=100)
    lat=models.CharField(max_length=100)
    datePlanted=models.CharField(max_length=60)
    lastChecked=models.CharField(max_length=60)
    status=models.CharField(max_length=60)
    about=models.CharField(max_length=200)

