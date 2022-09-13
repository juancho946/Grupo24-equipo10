import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from modeloRelacionalBaseDeDatos.models import Empresas
from django.http import JsonResponse
#from django.shortcuts import render

# Create your views here.

class EmpresasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)
    
    def get(self,request,id_empresas=""):

        if len(id_empresas)>0:
            empresa=list(Empresas.object.filter(Id_empresas=id_empresas).values())
            if len(empresa)>0:
                datos={'Empresa':empresa}

            else:
                datos={'mensaje': "No se encontro la Empresa."}
        
        else:
            empresas=list(Empresas.objects.values())
            if len(empresas)>0:
                datos={"mensaje":Empresas}
            else:
                datos={"mensaje":"No se encontraron Empresas."}

        return JsonResponse(datos)


    def post(self,request):
            data=json.loads(request.body)
            empresa=Empresas(id_empresas=data['id_empresas'],nombre=data['nombre'],ciudad=data['ciudad'],nit=data['nit'],sector_produc=data['sector_produc'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
            empresa.save()
            datos={'mensaje': 'Empresa Registrada Exitosamente'}
            return JsonResponse(datos)
        
    def put(self,request,id_empresas):
            data=json.loads(request.body)
            empresa=list(Empresas.objects.filter(Id_empresas=id_empresas).values())
            if len (empresa>0):
                emp=Empresas.objects.get(Id_empresas=id_empresas)
                emp.nombre=data["nombre"]
                emp.direccion=data["direccion"]
                emp.ciudad =data["ciudad"]
                emp.nit = data["nit"]
                emp.sector_produc= data["sector_produc"]
                emp.telefono = data["telefono"]
                emp.fecha_creacion =data["fecha_creacion"]
                emp.save()
                mensaje = {"mensaje":"Empresa actualizada exitosamente"}
            else:
                mensaje={"mensaje":"No se encontro la empresa"}
            
            return JsonResponse(mensaje)