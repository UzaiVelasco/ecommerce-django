from django.urls import path, include
from . import views #el punto es que esta en el mismo nivel del directorio

urlpatterns = [    
    path('', views.tienda, name="store"),
    #sera para categorias
    path('<slug:category_slug>/', views.tienda, name='products_by_category'),
    #esta ruta ayudara a agregarle a la qe ya tenemos de store, un produt_slug
    #que servira para almacenar un id y de esta
    # manera traer mediante consultas a la bd sus datos
    #en una nueva view
    #http://127.0.0.1:8000/store/ropa-de-verano/product-sulg 
    path('<slug:category_slug>/<slug:product_slug>/', views.product_detail, name='product_detail'),
]
