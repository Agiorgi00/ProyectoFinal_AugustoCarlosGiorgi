from django.db import models

class Restaurante(models.Model):
    nombre = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.nombre


class Menu(models.Model):
    nombre = models.CharField(max_length=255, unique=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre


class Plato(models.Model):
    nombre = models.CharField(max_length=100)
    #restaurante = models.ForeignKey(Restaurante, on_delete=models.CASCADE)
    menu = models.ForeignKey(Menu, on_delete=models.CASCADE, related_name="platos")

    def __str__(self):
        return self.nombre