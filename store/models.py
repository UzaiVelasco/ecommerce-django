from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name = models.CharField(max_length=200, unique=True)
    slug = models.CharField(max_length=200, unique=True)
    description = models.TextField(max_length=500, blank=True)    
    price = models.IntegerField()
    images = models.ImageField(upload_to='photos/products')
    stock = models.IntegerField()
    is_available = models.BooleanField(default=True) #si esta disponible
    #categoria que sería la llave foranea
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #esto hara que si se elimina la categria todos los produtos
    #de esa categoria se eleiminara
    
    created_date = models.DateTimeField(auto_now_add=True) #ue agarre la del sistema
    modified_date = models.DateTimeField(auto_now=True)
    
    def get_url(self):
        #el product_detail viene del urls porque asi lo definimos
        return reverse('product_detail',args=[self.category.slug, self.slug])
        #obteniendo algo asi https://localhost:8000/store/computadora/ipad-pro    
    
    def __str__(self):
        return self.product_name
