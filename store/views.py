from django.shortcuts import render, get_object_or_404
#como quiero consultar productos
from .models import Product

from category.models import Category


# Create your views here.
def tienda(request, category_slug=None):
    try:
        categories = None
        products = None
    
        if category_slug!=None:
        #dentro de los paramteros el slug es un campo de la tabla
        #categoría, con esta función get_objector404
        #sirve para encontrar, dependiendo los paraetros, na determinada
        #lista, es como el select * from where slug='computadoras'
        
        #en este caso usa el campo slug de categoria
        #la columna slug(debe de ser tal cual
        # el nombre de la columna) la comparara con el categoru_slug 
        #que estamos pasando como parametro
        #todas las que encuntre las metera en la lista categories
        #pero si no encuntra nada, o la tabla esta mal
        #mandara un error 404
            categories=get_object_or_404(Category, slug=category_slug)
            products = Product.objects.filter(category=categories, is_available=True)
            prodcut_count = products.count()
    
        else:        
            products = Product.objects.all().filter(is_available=True)
            #algo adicional que para este caso quiero que me devuelva
            #es la cantidad total de productos que tengo 
            prodcut_count = products.count()
        
        data = {
            'products': products,
            'product_count': prodcut_count
        }
        
        return render(request, 'store/store_template.html', data) #enviara la data a usuariosList.
    except:
     #si ocurre un error qiero que dispare la excepcion
        return render(request, 'store/404.html')

def product_detail(request, category_slug, product_slug):  
    #antes de redirigir al detalle del producto
    #puede ser que el usuario ingrese manualmente e incorrectamente
    #una direccion de categorpia por ejemplo
    #/store/computtadoras/  "computtadoras" no esta registrada en 
    #bd, lo correcto es computadoras
    #entonces para estos casos por eso el try
    try:
        #lo que hace el get en los parametros
        #es que category__ (doble guion bajo)slug sirve para
        #buscar dentro del campo slug de la app category(con minuscula porque
        # es la app no el modelo) con el category_slug que esta pasando
        #como argumento a la funcion
        # y como segunda condicion es el slug (en este caso como estamos dentro de
        # la app store no es necesario poner store__slug, basta con solo slug ya que
        # entra al modelo directamente) lo comparara con el que pase como parametro
        single_product=Product.objects.get(category__slug=category_slug, slug=product_slug)
        #si creo la varianle sin error creara un diccionario con
        #sus datos    
        data = {
            'single_product': single_product,
        }
     
        #y ya lo mandamos al template 
        return render(request, 'store/product-detail.html', data)

    except Exception as err:
        #si ocurre un error qiero que dispare la excepcion
        return render(request, 'store/404.html')
        
    