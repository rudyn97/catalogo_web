import string
from urllib import request

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.mail.backends import console
from django.http import JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import ListView, CreateView, UpdateView, DeleteView

from core.erp.forms import ProductForm
from core.erp.mixins import ValidatePermissionRequiredMixin
from core.erp.models import Product, Category


def buscar_productos(request):
    template_name = 'productos/list.html'
    q = request.GET["q"]
    # console.log(q)
    productos = Product.objects.filter(active=True, name__icontains=q)
    categorias = Category.objects.filter(active=True)

    listado = []
    for pro in productos:
        ingredientes = []
        agregados = []
        for ingre in pro.ing.all():
            ingredientes.append(ingre)
        for agreg in pro.agre.all():
            agregados.append(agreg)

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
                'agreg': agregados,
            }
        }
        listado.append(item)

    context = {"productos": listado, "categorias": categorias}
    return render(request, template_name, context)


def listar_productos(request, nombre):
    template_name = 'productos/list.html'
    if nombre == 'general':
        productos = Product.objects.filter(active=True)
        # color = 'general'
    else:
        cat = Category.objects.get(name=nombre)
        productos = Product.objects.filter(active=True, cate=cat)
        # color = ''

    listado = []
    for pro in productos:
        ingredientes = []
        agregados = []
        for ingre in pro.ing.all():
            ingredientes.append(ingre.name)
        for agreg in pro.agre.all():
            agregados.append(agreg)
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
                'agreg': agregados,
            }
        }
        listado.append(item)

    categorias = Category.objects.filter(active=True)
    # context = {"productos": productos, "categorias": categorias, "color": color}
    context = {"productos": listado, "categorias": categorias}
    return render(request, template_name, context)


class ProductListView(LoginRequiredMixin, ValidatePermissionRequiredMixin, ListView):
    model = Product
    template_name = 'productos/list.html'
    permission_required = 'erp.view_product'

    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = Product.objects.all()
        try:
            action = request.POST['action']
            if action == 'searchdata':
                data = []
                for i in Product.objects.all():
                    data.append(i.toJSON())
            else:
                data['error'] = 'Ha ocurrido un error'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data, safe=False)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Listado de Productos'
        context['create_url'] = reverse_lazy('erp:product_create')
        context['list_url'] = reverse_lazy('erp:product_list')
        context['entity'] = 'Productos'
        return context


class ProductCreateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    template_name = 'productos/create.html'
    success_url = reverse_lazy('erp:product_list')
    permission_required = 'erp.add_product'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'add':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Creación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = self.success_url
        context['action'] = 'add'
        return context


class ProductUpdateView(LoginRequiredMixin, ValidatePermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    template_name = 'productos/create.html'
    success_url = reverse_lazy('erp:product_list')
    permission_required = 'erp.change_product'
    url_redirect = success_url

    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            action = request.POST['action']
            if action == 'edit':
                form = self.get_form()
                data = form.save()
            else:
                data['error'] = 'No ha ingresado a ninguna opción'
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Edición de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = self.success_url
        context['action'] = 'edit'
        return context


class ProductDeleteView(LoginRequiredMixin, ValidatePermissionRequiredMixin, DeleteView):
    model = Product
    template_name = 'productos/delete.html'
    success_url = reverse_lazy('erp:product_list')
    permission_required = 'erp.delete_product'
    url_redirect = success_url

    @method_decorator(login_required)
    def dispatch(self, request, *args, **kwargs):
        self.object = self.get_object()
        return super().dispatch(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        data = {}
        try:
            self.object.delete()
        except Exception as e:
            data['error'] = str(e)
        return JsonResponse(data)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Eliminación de un Producto'
        context['entity'] = 'Productos'
        context['list_url'] = self.success_url
        return context
