from django.shortcuts import render

from core.erp.models import *


def ver_productos(request, id):
    template_name = 'detalles/view.html'
    productos = Product.objects.filter(active=True, id=id)
    categorias = Category.objects.filter(active=True)

    listado = []
    for pro in productos:
        ingredientes = []
        for ingre in pro.ing.all():
            ingredientes.append(ingre.name)
        item = {
            'producto': {
                'id': pro.id,
                'name': pro.name,
                'get_image': pro.get_image,
                'desc': pro.desc,
                'pvp': pro.pvp,
                'cate': pro.cate,
                # 'ingre': pro.ing.all(),
                'ingre': ingredientes,
            }
        }
        listado.append(item)

    context = {"productos": listado, "categorias": categorias}
    return render(request, template_name, context)


def view_general(request):
    template_name = 'detalles/view_total.html'
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
            for ingre in pro.ing.all():
                ingredientes.append(ingre.name)
            # ingr = []
            # for ing in ingredientes:
            #     ingr.append(ing)
            # # GUARDAR EL PRODUCTO
            item = {
                'producto': {
                    'id': pro.id,
                    'name': pro.name,
                    'get_image': pro.get_image,
                    'desc': pro.desc,
                    'pvp': pro.pvp,
                    'cate': pro.cate,
                    # 'ingre': pro.ing.all(),
                    'ingre': ingredientes,
                }
            }
            listado.append(item)
        item1 = {
            'categ': {
                'cat': c.name,
                'cat_prod': listado
            }
        }
        # Supuestamente aqui tengo los item1
        # las categorias como categ dentro de los item
        # y dentro la categoria y un listado de sus productos
        if len(listado) != 0:
            total.append(item1)

    context = {'total_cat_pro': total, 'categorias': categorias}
    return render(request, template_name, context)
