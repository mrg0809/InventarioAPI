from django.db import models
from django.db.models.fields import CharField
from django.db.models.fields.related import ForeignKey

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class SubCategoria(models.Model):
    nombre = models.CharField(max_length=30)
    
    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Marca(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class Familia(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre


class SubFamilia(models.Model):
    nombre = models.CharField(max_length=30)

    class Meta:
        ordering = ('nombre',)

    def __str__(self):
        return self.nombre

class Articulo(models.Model):
    modelo = models.CharField(max_length=18)
    marca = models.ForeignKey(Marca, related_name='marca', on_delete=models.SET_DEFAULT, default=1)
    familia = models.ForeignKey(Familia, related_name='related_familia', on_delete=models.SET_DEFAULT, default=1)
    subfamilia = models.ForeignKey(SubFamilia, related_name='subfamilia', on_delete=models.SET_DEFAULT, default=1)
    categoria = models.ForeignKey(Categoria, related_name='related_categoria', on_delete=models.SET_DEFAULT, default=1)
    subcategoria = models.ForeignKey(SubCategoria, related_name='related_subcategoria', on_delete=models.SET_DEFAULT, default=1)
    descripcion = models.TextField(blank=True, null=True)
    precio = models.DecimalField(max_digits=6, decimal_places=2)
    preciodescuento = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)

    def __str__(self):
        return self.modelo


class VarianteArticulo(models.Model):
    padre = ForeignKey(Articulo, on_delete=models.CASCADE, null=True)
    talla = models.CharField(max_length=5)  #S, M, L ,21, 22
    inventario = models.IntegerField(default=0)
    upc = models.CharField(max_length=15, unique=True)

    class Meta:
        unique_together = (
            ('padre', 'talla')
        )

    def __str__(self):
        return self.talla