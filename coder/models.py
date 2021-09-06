from django.db import models


class Projects(models.Model):
    name=models.CharField(max_length=100)
    longnameurl=models.CharField(max_length=200,null=True)
    technologies=models.CharField(max_length=100)
    htmlpage=models.CharField(max_length=100,null=True)
    price=models.PositiveIntegerField(null=True)
    poster=models.ImageField(upload_to='projectposter/',null=True,blank=True)
    shortdescription=models.CharField(max_length=100,null=True)
    downloadlink=models.CharField(max_length=200,null=True)
    def __str__(self):
        return self.name
