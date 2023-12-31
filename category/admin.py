from django.contrib import admin
from .models import Category
# Register your models here.


#
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('category_name',)} #Esto para que se rellene automaticamnet
    #con los datos de nombre de categoria
    list_display = ('category_name','slug')

    
    
admin.site.register(Category, CategoryAdmin)