from django.shortcuts import render
from store.models import Product

def home(request):
    #antes de redirigir a la pagina de home
    #teneos que traer los productos que 
    #estan en la bd pero trayendo solo los que 
    #estan activos. Tenemos una columna
    #dentro de productos para ver si estan activos
    products = Product.objects.all().filter(is_available=True)
    
    #lo envolvemos en un diccionario
    context = {
        'products': products,
    }
    
    return render(request,"home.html", context)