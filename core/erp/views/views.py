from django.contrib.messages.storage import session
from django.shortcuts import render
from django.views.generic import TemplateView
from django.urls import reverse_lazy

from core.erp.models import *


class IndexView(TemplateView):
    template_name = 'body.html'


def view_general(request):
    template_name = 'body.html'
    # prod = Product.objects.filter(active=True)
    categorias = Category.objects.filter(active=True)
    total = []
    for c in categorias:
        productos = Product.objects.filter(active=True, cate=c.id)
        # TENGO TODOS LOS PROD PARA LA CAT DE ARRIBA
        listado = []
        for pro in productos:
            # ingredientes = Ingredient.objects.filter(active=True)
            # pr = Product.objects.filter(active=True, ing__id=ingredientes.id)
            # AGREGAR LISTADO DE INGREDIENTES
            ingredientes = []
            agregados = []
            for ingre in pro.ing.all():
                ingredientes.append(ingre.name)
            for agreg in pro.agre.all():
                agregados.append(agreg.name)
            # # GUARDAR EL PRODUCTO
            item = {
                'producto': {
                    'id': pro.id,
                    'name': pro.name,
                    'get_image': pro.get_image,
                    'desc': pro.desc,
                    'pvp': pro.pvp,
                    'cate': pro.cate,
                    'ingre': ingredientes,
                    'agreg': agregados,
                }
            }
            listado.append(item)
        item1 = {
            'categ': {
                'cat': c.name,
                'desc': c.desc,
                'cat_prod': listado
            }
        }
        # Supuestamente aqui tengo los item1
        # las categorias como categ dentro de los item
        # y dentro la categoria y un listado de sus productos
        if len(listado) != 0:
            total.append(item1)

    context = {'todo_prod': total, 'categorias': categorias}
    return render(request, template_name, context)


def view_productos(request, id):
    template_name = 'view_product.html'
    # prod = Product.objects.filter(active=True)
    categorias = Category.objects.filter(active=True)
    productos = Product.objects.filter(active=True, id=id)
    # TENGO TODOS LOS PROD PARA LA CAT DE ARRIBA
    listado = []
    for pro in productos:
        # AGREGAR LISTADO DE INGREDIENTES
        ingredientes = []
        agregados = []
        for ingre in pro.ing.all():
            ingredientes.append(ingre.name)
        for agreg in pro.agre.all():
            agregados.append(agreg)
        # # GUARDAR EL PRODUCTO
        item = {
            'producto': {
                'id': pro.id,
                'name': pro.name,
                'get_image': pro.get_image,
                'desc': pro.desc,
                'pvp': pro.pvp,
                'cate': pro.cate,
                'ingre': ingredientes,
                'agreg': agregados,
            }
        }
        listado.append(item)

    context = {'todo_prod': listado, 'categorias': categorias}
    return render(request, template_name, context)
