from django.db import models


class Projects(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=2000)
    technologies=models.CharField(max_length=100)
    youtubelink=models.CharField(max_length=500)
    price=models.CharField(max_length=20)
    poster=models.ImageField(upload_to='projectposter/',null=True,blank=True)
    shortdescription=models.CharField(max_length=100,null=True)
    downloadlink=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
