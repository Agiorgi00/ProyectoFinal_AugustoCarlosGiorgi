from django.shortcuts import render, redirect, get_object_or_404
from .forms import RestauranteForm, MenuForm, PlatoForm, RestauranteSearchForm
from .models import Restaurante, Menu, Plato
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import RegisterForm
from django.contrib.auth import logout


def Base(request):
    return render(request, "Base.html")


def restaurante(request):
    if request.method == "POST":
        form = RestauranteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = RestauranteForm()
    return render(request, "restaurante.html", {"form": form})


def buscar_restaurante(request):
    form = RestauranteForm()
    resultados = None
    if "query" in request.GET:
        form = RestauranteForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data["query"]
            resultados = Restaurante.objects.filter(nombre__icontains=query)
    return render(request, "buscar_restaurante.html", {"form": form, "resultados": resultados})


def lista_restaurantes(request):
    restaurantes = Restaurante.objects.all()
    return render(request, "lista_restaurante.html", {"restaurantes": restaurantes})


def editar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == "POST":
        form = RestauranteForm(request.POST, instance=restaurante)
        if form.is_valid():
            form.save()
            return redirect("lista_restaurante")
    else:
        form = RestauranteForm(instance=restaurante)
    return render(request, "editar_restaurante.html", {"form": form})


def eliminar_restaurante(request, pk):
    restaurante = get_object_or_404(Restaurante, pk=pk)
    if request.method == "POST":
        restaurante.delete()
        return redirect("lista_restaurante")
    return render(request, "confirmar_eliminacion.html", {"obj": restaurante})


def menus(request):
    if request.method == "POST":
        form = MenuForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = MenuForm()
    return render(request, "menu.html", {"form": form})


def buscar_menus(request):
    query = request.GET.get("q")
    menus = []
    if query:
        menus = Menu.objects.filter(nombre__icontains=query)
    return render(request, "buscar_menu.html", {"menus": menus, "query": query})


def lista_menus(request):
    menus = Menu.objects.all()
    return render(request, "lista_menu.html", {"menus": menus})


def editar_menus(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        form = MenuForm(request.POST, instance=menu)
        if form.is_valid():
            form.save()
            return redirect("lista_menus")
    else:
        form = MenuForm(instance=menu)
    return render(request, "editar_menu.html", {"form": form})


def eliminar_menus(request, pk):
    menu = get_object_or_404(Menu, pk=pk)
    if request.method == "POST":
        menu.delete()
        return redirect("lista_menus")
    return render(request, "confirmar_eliminacion.html", {"obj": menu})


def platos(request):
    if request.method == "POST":
        form = PlatoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("Base")
    else:
        form = PlatoForm()
    return render(request, "platos.html", {"form": form})


def buscar_platos(request):
    query = request.GET.get("query", "")
    if query:
        platos = Plato.objects.filter(nombre__icontains=query)
    else:
        platos = []
    return render(request, "buscar_plato.html", {"platos": platos})


def lista_platos(request):
    platos = Plato.objects.all()
    return render(request, "lista_platos.html", {"platos": platos})


def editar_platos(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        form = PlatoForm(request.POST, instance=plato)
        if form.is_valid():
            form.save()
            return redirect("lista_platos")
    else:
        form = PlatoForm(instance=plato)
    return render(request, "editar_plato.html", {"form": form})


def eliminar_platos(request, pk):
    plato = get_object_or_404(Plato, pk=pk)
    if request.method == "POST":
        plato.delete()
        return redirect("lista_platos")
    return render(request, "confirmar_eliminacion.html", {"obj": plato})


def registro(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password1")
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect("Base")
    else:
        form = RegisterForm()
    return render(request, "registro.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("Base")
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("Base")