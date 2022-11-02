"""Proyecto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from Proyecto.views import index,ListadoClientes,ClienteInsertar,Borrarcliente,Actualizarcliente
from Proyecto.views import FacturaInsertar

urlpatterns = [
    path('admin/', admin.site.urls),
    path('inicio/',index),
    path('Cliente/listado/',ListadoClientes),
    path('Cliente/insertar1/',ClienteInsertar),
    path('Cliente/borrar/<int:id>',Borrarcliente),
    path('Cliente/actualizar/<int:id>',Actualizarcliente),
    path('Factura/insertar/',FacturaInsertar),
]
