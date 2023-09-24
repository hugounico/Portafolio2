from django.db import models

# Create your models here.
class Project(models.Model):
    title = models.CharField(max_length=150)            #puedo agregar en el () para elegir el nombre eb admin (max_length=150, verbose_name='name')) 
    Description = models.TextField()                    #en text field no es necesario elegir la longitud maxima
    image = models.ImageField(upload_to='projects')     #necesita instalar Pillow
    link = models.URLField(max_length=250, null=True)   #URL es para agregar links ocn django
    created = models.DateTimeField(auto_now_add=True)   #campos de fecha y hora que usaremos para orderan los proyectos por fecha
    update = models.DateTimeField(auto_now=True)        #auto_now_add graba cuando creamos el registro /auto_now se actualiza cuando se graban cambios
    
    class Meta:
        ordering = ['-created']                          #para que los proyectos se ordenen de manera ascendente (manejar con simbolo -)

    def __str__(self):
        return self.title