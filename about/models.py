from django.db import models

# Create your models here.
class Course(models.Model):
    title = models.CharField(max_length=150)             
    year = models.IntegerField()
    Institution = models.TextField() 
    Description = models.TextField()                    
    created = models.DateTimeField(auto_now_add=True)   
    update = models.DateTimeField(auto_now=True) 

    class Meta:
        ordering = ['-created']                          

    def __str__(self):
        return self.title
    
class Skill(models.Model):
    title = models.CharField(max_length=150)
    image = models.ImageField(upload_to='about')
    created = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title