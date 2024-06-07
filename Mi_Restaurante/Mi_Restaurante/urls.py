"""
URL configuration for Mi_Restaurante project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from Restaurante import views as Restaurante_views
from Restaurante.views import registro, login_view
from django.contrib.auth.views import LogoutView


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", Restaurante_views.Base, name="Base"),
    path("login", Restaurante_views.login_view, name="login_view"),
    path("logout", Restaurante_views.logout_view, name="logout_view"),
    path("registro", Restaurante_views.registro, name="registro"),
    path("restaurante", Restaurante_views.restaurante, name="restaurante"),
    path("buscar_restaurante", Restaurante_views.buscar_restaurante, name="buscar_restaurante"),
    path("lista_restaurante", Restaurante_views.lista_restaurantes, name="lista_restaurante"),
    path("editar_restaurante/<int:pk>/", Restaurante_views.editar_restaurante, name="editar_restaurante"),
    path("eliminar_restaurante/<int:pk>/", Restaurante_views.eliminar_restaurante, name="eliminar_restaurante"),
    path("menus", Restaurante_views.menus, name="menus"),
    path("buscar_menus", Restaurante_views.buscar_menus, name="buscar_menus"),
    path("lista_menus", Restaurante_views.lista_menus, name="lista_menus"),
    path("editar_menus/<int:pk>/", Restaurante_views.editar_menus, name="editar_menus"),
    path("eliminar_menus/<int:pk>/", Restaurante_views.eliminar_menus, name="eliminar_menus"),
    path("platos", Restaurante_views.platos, name="platos"),
    path("buscar_platos", Restaurante_views.buscar_platos, name="buscar_platos"),
    path("lista_platos", Restaurante_views.lista_platos, name="lista_platos"),
    path("editar_platos/<int:pk>/", Restaurante_views.editar_platos, name="editar_platos"),
    path("eliminar_platos/<int:pk>/", Restaurante_views.eliminar_platos, name="eliminar_platos"),
]

