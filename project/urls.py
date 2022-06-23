"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from app.views import home, create, store, painel, logar, dashboard, deslogar, administrador, usuario, contato, endereco, veiculo, criarCliente, criarEndereco, criarVeiculo, view, editCliente, editEndereco, editVeiculo, updateCliente, updateEndereco, updateVeiculo, deleteCliente, senha, changePassword


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('create/', create),
    path('store/', store),
    path('painel/', painel),
    path('login/', logar),
    path('dashboard/', dashboard),
    path('deslogar/', deslogar),
    path('home/', home),
    path('administrador/index', administrador, name='admin'),
    path('usuario/formulario', usuario),
    path('contato/', contato),
    path('usuario/endereco', endereco, name='endereco'),
    path('usuario/veiculo', veiculo, name='veiculo'),
    path('criarCliente/', criarCliente),
    path('criarEndereco/', criarEndereco),
    path('criarVeiculo/', criarVeiculo),
    path('usuario/view/<int:pk>/', view, name='view'),
    path('usuario/editCliente/<int:pk>/', editCliente, name='editCliente'),
    path('usuario/editEndereco/<int:pk>/', editEndereco, name='editEndereco'),
    path('usuario/editVeiculo/<int:pk>/', editVeiculo, name='editVeiculo'),
    path('updateCliente/<int:pk>/', updateCliente, name='updateCliente'),
    path('updateEndereco/<int:pk>/', updateEndereco, name='updateEndereco'),
    path('updateVeiculo/<int:pk>/', updateVeiculo, name='updateVeiculo'),
    path('usuario/deleteCliente/<int:pk>/', deleteCliente, name='deleteCliente'),
    path('senha/', senha),
    path('changePassword/', changePassword),
    path('administrador/', administrador)


]
