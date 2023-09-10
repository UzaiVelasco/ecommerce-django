from django.db import models
from django.urls import reverse

# Create your models here.
class Category(models.Model):
    category_name = models.CharField(max_length=20, unique=True)#que no acepte valores repetidos
    description = models.CharField(max_length=255, blank=True)#que permita valores nulos
    slug= models.CharField(max_length=100, unique=True)#destinado a la parte final de la url que representa a la entidad
    category_image=models.ImageField(upload_to='photos/categories', blank=True) #que permita nulos
    
    #para cambiarle el nombre que a la tabla que le pone por
    #defecto django    
    class Meta:
        verbose_name='category'
        verbose_name_plural='categories'
    #Ojo como este cambio lo hicimos despues de haber echo ya la migracion
    #es volver a hacer el archivo y ejecutarlo
    
    #es una funcion para retornar la url con ayuda del reverd
    #trayendo el slug products_by_category que esta en urls de store
    #junto con el argumento de slug del objeto categoria(self)
    def get_url(self):
        return reverse('products_by_category',args=[self.slug])
        #obteniendo algo asi https://localhost:8000/store/computadora
    
    def __str__(self):
        return self.category_name    