"""cofig URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.urls import path, include

from core.erp.views.categorias.views import CategoryListView, listar_categorias
from core.erp.views.productos.views import ProductListView
# from core.login.views import *

from django.conf import settings
from django.conf.urls.static import static

from core.erp.views.views import IndexView, view_general, view_productos

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', IndexView.as_view(), name='index'),
    path('', view_general, name='index'),
    path('<id>/', view_productos, name='product_view')

    # path('', listar_categorias, name='index'),
    # path('erp/', include('core.erp.urls'), name='index'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
