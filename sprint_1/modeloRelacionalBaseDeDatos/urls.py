from django.urls import path
from modeloRelacionalBaseDeDatos.views import EmpresasView

urlpatterns=[
    path('Empresas/',EmpresasView.as_view(),name='Listar'),
    path('Empresas/<str:Id_empresas>', EmpresasView.as_view(),name='Insert'),
    path('Empresas/<str:Id_empresas>', EmpresasView.as_view(),name='Buscar')   
]