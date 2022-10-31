from ast import If
from multiprocessing import context
from re import template
from django.http import HttpResponse
from django.template import Template,Context
from Proyecto.models import Cliente
from django.db import connection
from django.shortcuts import render,redirect
from django.contrib import messages

def index(request):
    return HttpResponse("Hola Mundo! o Hello  World!")

def ListadoClientes(request):
    archivobase = open("Proyecto/Template/Cliente/listaclientes.html")
    lectura = Template(archivobase.read()) 
    archivobase.close()
    clientes=Cliente.objects.all()
    parametros = Context({'clientes':clientes})
    paginaresultado = lectura.render(parametros)
    return HttpResponse(paginaresultado)

def ClienteInsertar(request):
    if request.method=="POST":
        if request.POST.get('nombre') and request.POST.get('apellido') and request.POST.get('edad') and request.POST.get('celular') and request.POST.get('fech_nac') and request.POST.get('email') and request.POST.get('genero') and request.POST.get('cedula'):
            clientes= Cliente()
            clientes.nombre= request.POST.get('nombre') 
            clientes.apellido= request.POST.get('apellido') 
            clientes.edad= request.POST.get('edad') 
            clientes.celular= request.POST.get('celular') 
            clientes.fech_nac= request.POST.get('fech_nac') 
            clientes.email= request.POST.get('email') 
            clientes.genero= request.POST.get('genero') 
            clientes.cedula= request.POST.get('cedula')
            insertar=connection.cursor()
            insertar.execute("call insertarclientes('"+clientes.nombre+"','"+clientes.apellido+"','"+clientes.edad+"','"+clientes.celular+"','"+clientes.fech_nac+"','"+clientes.email+"','"+clientes.genero+"','"+clientes.cedula+"')")
            messages.success(request, "El usuario: " + clientes.nombre + " se guardó con exito")
            return render(request,'Cliente/insertar.html')
    else:
        return render(request,'Cliente/insertar.html')

def Borrarcliente(request,id):
    cliente=Cliente.objects.get(id=id)
    cliente.delete()
    return redirect("/cliente/listado/")