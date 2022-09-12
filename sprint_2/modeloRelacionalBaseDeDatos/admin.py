from django.contrib import admin
from modeloRelacionalBaseDeDatos.models import Administrador
from modeloRelacionalBaseDeDatos.models import Empresas
from modeloRelacionalBaseDeDatos.models import Empleado

admin.site.register(Administrador)
admin.site.register(Empresas)
admin.site.register(Empleado)

# Register your models here.
