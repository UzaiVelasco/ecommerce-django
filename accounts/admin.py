from django.contrib import admin
from .models import Account

#este import sera para todas esas configuraciones
from django.contrib.auth.admin import UserAdmin

#Las configuraciones que hare aqui van a servir para 
#que en el admin de django se vea no solo el nombre
#del correo del usuario, si no tambien
#configurar que se vea si es usuario activo, 
#cuando fue la ultima fecha de ingreso, 
#y que desde el panel la contraseña solo pueda ser leida y no
#editada

class AccountAdmin(UserAdmin):
    #estas son las propiedades que quiero que se vean en el djnago admin
    list_display = ('email', 'first_name','last_name','username', 'last_login','date_joined','is_active')
    #este ayudara para cuando el usuario le de clic a una columna en particular
    #lo linkee a ese dato
    list_display_link = ('email','first_name','last_name')
    #solo las qie sean de lectura
    readonly_fields = ('last_login','date_joined')
    ordering = ('-date_joined',) #ordenara asecendente los registros, 
    #de acuerdo a la columna date joined, es decir el dia que se unio
    
    #estos tres solo se inicializaran
    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()
    
# Register your models here.
admin.site.register(Account, AccountAdmin)