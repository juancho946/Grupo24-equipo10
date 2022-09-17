#from django.shortcuts import render
import json
from django.views import View
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from modeloRelacionalBaseDeDatos.models import Empresas,Empleado,Reporte_contable,Rol
from django.http import JsonResponse



#____________________TABLA EMPRESAS______________________

class EmpresasView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

        #FUNCION PARA OBTENER EMPRESAS
    
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

    
            #FUNCION PARA CREAR EMPRESAS

    def post(self,request):
            data=json.loads(request.body)
            empresa=Empresas(id_empresas=data['id_empresas'],nombre=data['nombre'],ciudad=data['ciudad'],nit=data['nit'],sector_produc=data['sector_produc'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
            empresa.save()
            datos={'mensaje': 'Empresa Registrada Exitosamente'}
            return JsonResponse(datos)

            #FUNCION PARA EDITAR EMPRESAS
        
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

#______________________TABLA ROL______________________


class RolView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request,*args,**kwargs)

        #FUNCION PARA OBTENER UN ROL
    
    def get(selft,request,Id_rol=""):

        if len(Id_rol)>0:
            rol=list(Rol.object.filter(id_rol=Id_rol).values())
            if len(rol)>0:
                datos={'Rol':rol}

            else:
                datos={'mensaje': "No se encontró el Rol."}
        
        else:
            Roles=list(Rol.objects.values())
            if len(Roles)>0:
                datos={"mensaje":Roles}
            else:
                datos={"mensaje":"No se encontro el Rol."}

        return JsonResponse(datos)

    

#____________________TABLA EMPLEADOS______________________
    
class EmpleadoView(View):
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)


        #FUNCION PARA OBTENER EMPLEADOS      

    def get(self,request,idempleado=""):

        if len(idempleado)>0:
            empleado=list(Empleado.objects.filter(id_empleado=idempleado).values())
            if len(empleado)>0:
                datos={'Empleado': empleado}
            else:
                datos={'mensaje': 'No se encontraron empleados'}
        else:
            empleado=list(Empleado.objects.values()) 
            if len(empleado)>0:
                datos={"mensaje":empleado}
            else:
                datos={"mensaje":"No se encontraron empleados."}

        return JsonResponse(datos)


        #FUNCION PARA AGREGAR EMPLEADOS

    def post (self,request):
        data=json.loads(request.body)
        print(data)
        roles=Rol.objects.get(id_rol=data["rol"])
        empre=Empresas.objects.get(id_empresas=data["empresas_id"])
        emple=Empleado.objects.create(id_empleado=data["id_empleado"],empresas_id=empre, rol=roles,nombre=data['nombre'],apellido=data['apellido'],email=data['email'],telefono=data['telefono'],fecha_creacion=data['fecha_creacion'])
        emple.save()
        mensaje={"Mensaje":"Empleado registrado exitosamente"}

        return JsonResponse(mensaje)
        
        #FUNCION PARA EDITAR EMPLEADOS

    def put(self,request,id_empleado):
            data=json.loads(request.body)
            empleado=list(Empleado.objects.filter(Id_empleado=id_empleado).values())
            if len (empleado)>0:
                emp=Empleado.objects.get(Id_empleado=id_empleado)
                emp.nombre=data["nombre"]
                emp.apellido=data["apellido"]
                emp.email =data["email"]
                emp.telefono = data["telefono"]
                emp.empresas_id = data["empresas_id"]
                emp.fecha_creacion =data["fecha_creacion"]
                emp.save()
                mensaje = {"mensaje":"Empleado actualizado exitosamente"}
            else:
                mensaje={"mensaje":"No se encontro el Empleado"}
            
            return JsonResponse(mensaje)

#____________________TABLA REPORTE CONTABLE______________________

class Reporte_contableView(View):

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

        #FUNCION PARA OBTENER REPORTE CONTABLE

    def get(self,request,idestado=""):

        if len(idestado)>0:
            estado=list(Reporte_contable.objects.filter(id_estado=idestado).values())
            if len(estado)>0:
                datos={'Estado':estado}
            else:
                datos={'mensaje':"No se encontró el Estado Financiero."} 
        else:
            estado=list(Reporte_contable.objects.values())
            if len(estado)>0:
                datos={"mensaje":estado}
            else:
                datos={"mensaje":"No se encontro ningun Reporte."}

        return JsonResponse(datos)

