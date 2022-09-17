from django.urls import path
from modeloRelacionalBaseDeDatos.views import EmpleadoView, EmpresasView, RolView, EmpleadoView

urlpatterns = [
    path('Empresas/', EmpresasView.as_view(), name= 'Listar'),
    path('Empresas/<str:idempresas>', EmpresasView.as_view(), name= 'Buscar'), #esta ruta nos sirve para consultar, agregar, actualizar y eliminar las empresas
    path('Empleado/', EmpleadoView.as_view(), name= 'Buscar'),
    path('Rol/',RolView.as_view(), name= 'Rol'),
]
