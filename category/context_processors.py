#va a servir para el filtrado de categoias
from .models import Category

def menu_links(request):
    links = Category.objects.all()
    return dict(links=links) #esta palabra dict es un metodo que geenera un diccionario
    #con el nombre en este caso links = a lo que ya alamaceno 
    #nuestra variable links

    