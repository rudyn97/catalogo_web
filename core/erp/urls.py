from django.urls import path

from core.erp.views.categorias.views import *
from core.erp.views.detalles.views import ver_productos
# from core.erp.views.detalles.views import ver_productos, view_general
# from core.erp.views.clientes.views import *
# from core.erp.views.dashboard.views import DashboardView
from core.erp.views.productos.views import *
# from core.erp.views.tests.views import TestView

app_name = 'erp'

urlpatterns = [

    #Catalogo
    path('', listar_categorias, name='category_list'),
    # path('detalles/<id>', ver_productos, name='product_view'),

    # path('<nombre>/', listar_productos, name='product_list'),
    # path('b', buscar_productos, name='buscar'),
    # path('detail/<id>/', ver_productos, name='product_view'),
    # path('total/general/', view_general, name='product_view_general'),


    # Categorias
    # path('categorias/list/', CategoryListView.as_view(), name='category_list'),

    # path('categorias/add/', CategoryCreateView.as_view(), name='category_create'),
    # path('categorias/update/<int:pk>/', CategoryUpdateView.as_view(), name='category_update'),
    # path('categorias/delete/<int:pk>/', CategoryDeleteView.as_view(), name='category_delete'),
    # path('categorias/list/', search, name='category_list'),

    # path('categorias/form/', CategoryFormView.as_view(), name='category_form'),

    # Clientes
    # path('clientes/list/', ClientListView.as_view(), name='client_list'),
    # path('clientes/add/', ClientCreateView.as_view(), name='client_create'),
    # path('clientes/update/<int:pk>/', ClientUpdateView.as_view(), name='client_update'),
    # path('clientes/delete/<int:pk>/', ClientDeleteView.as_view(), name='client_delete'),

    # Productos
    # path('productos/list/', ProductListView.as_view(), name='product_list'),

    # path('productos/add/', ProductCreateView.as_view(), name='product_create'),
    # path('productos/update/<int:pk>/', ProductUpdateView.as_view(), name='product_update'),
    # path('productos/delete/<int:pk>/', ProductDeleteView.as_view(), name='product_delete'),


    # Home
    # path('dashboard/', DashboardView.as_view(), name='dashboard'),

    # Tests
    # path('test/', TestView.as_view(), name='tests'),
]


