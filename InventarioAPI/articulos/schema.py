from django.db.models import fields
import graphene
from graphene_django import DjangoObjectType
from .models import Articulo, VarianteArticulo

class ArticuloType(DjangoObjectType):
    class Meta:
        model = Articulo
        fields = ('id', 'modelo', 'marca', 'familia', 'subfamilia', 'categoria', 'subcategoria')

class VarianteArticuloType(DjangoObjectType):
    class Meta:
        model = VarianteArticulo
        fields = ('upc', 'talla')

class Query(graphene.ObjectType):

    all_articulos = graphene.List(ArticuloType)