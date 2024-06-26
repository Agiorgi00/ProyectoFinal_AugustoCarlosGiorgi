from django import forms
from .models import Restaurante, Menu, Plato
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class RestauranteForm(forms.ModelForm):
    class Meta:
        model = Restaurante
        fields = ["nombre"]


class MenuForm(forms.ModelForm):
    class Meta:
        model = Menu
        fields = ["nombre", "restaurante"]


class PlatoForm(forms.ModelForm):
    class Meta:
        model = Plato
        fields = ["nombre", "menu"]


class RestauranteSearchForm(forms.Form):
    query = forms.CharField(label="Buscar Restaurante", max_length=255)


class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Correo Electrónico", help_text="Por favor, introduce tu correo electrónico.")

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(RegisterForm, self).__init__(*args, **kwargs)
        self.fields["username"].label = "Nombre de Usuario"
        self.fields["password1"].label = "Contraseña"
        self.fields["password2"].label = "Confirmación de contraseña"
        self.fields["username"].help_text = (
            "Requerido. 150 caracteres o menos. Solo se permiten letras, dígitos y los siguientes caracteres: @/./+/-/_"
        )
        self.fields["password1"].help_text = "Tu contraseña debe tener al menos 8 caracteres."
        self.fields["password2"].help_text = "Repite la misma contraseña."


