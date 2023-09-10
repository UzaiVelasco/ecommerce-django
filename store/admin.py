from django.contrib import admin
from .models import Product

#para las propiedades personalizadas

class ProductAdmin(admin.ModelAdmin):
    list_display = ('product_name','price', 'stock', 'category', 'modified_date','is_available')
    #para que el slug se auto llene al ingresar el nombre del producto
    prepopulated_fields = {'slug':('product_name',)}

# Register your models here.
admin.site.register(Product, ProductAdmin)