from crum import get_current_user
from django.db import models
from datetime import datetime

from django.forms import model_to_dict

from cofig.settings import MEDIA_URL, STATIC_URL
from core.erp.choices import gender_choices
from core.models import BaseModel


class Category(BaseModel):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Categoria'
        verbose_name_plural = 'Categorias'
        db_table = 'categoria'
        ordering = ['id']


class Ingredient(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='ingredient/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    active = models.BooleanField(default=True)
    # pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    # desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')
    # # color = models.DecimalField(default=1, max_digits=4, decimal_places=0, verbose_name='Color')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        # item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Ingrediente'
        verbose_name_plural = 'Ingredientes'
        db_table = 'ingrediente'
        ordering = ['id']


class Aggregate(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='ingredient/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    active = models.BooleanField(default=True)
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['image'] = self.get_image()
        # item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Agregado'
        verbose_name_plural = 'Agregados'
        db_table = 'agregado'
        ordering = ['id']


class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
    image = models.ImageField(upload_to='product/%Y/%m/%d', null=True, blank=True, verbose_name='Imagen')
    pvp = models.DecimalField(default=0.00, max_digits=9, decimal_places=2, verbose_name='Precio de venta')
    cate = models.ForeignKey(Category, on_delete=models.CASCADE, verbose_name="Categoria")
    ing = models.ManyToManyField(Ingredient, verbose_name="Ingrediente", blank=True)
    agre = models.ManyToManyField(Aggregate, verbose_name="Agregados", blank=True)
    desc = models.CharField(max_length=500, null=True, blank=True, verbose_name='Descripcion')
    # color = models.DecimalField(default=1, max_digits=4, decimal_places=0, verbose_name='Color')
    active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    def toJSON(self):
        item = model_to_dict(self)
        item['cate'] = self.cate.toJSON()
        item['ing'] = self.ing.toJSON()
        item['agre'] = self.agre.toJSON()
        item['image'] = self.get_image()
        item['pvp'] = format(self.pvp, '.2f')
        return item

    def get_image(self):
        if self.image:
            return '{}{}'.format(MEDIA_URL, self.image)
        return '{}{}'.format(STATIC_URL, 'img/empty.png')

    class Meta:
        verbose_name = 'Producto'
        verbose_name_plural = 'Productos'
        db_table = 'producto'
        ordering = ['id']


# class Sale(models.Model):
#
#     table = models.CharField(max_length=150, verbose_name='Nombre', unique=True)
#     product = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name='Producto')
#     cant = models.DecimalField(default=0, max_digits=9, decimal_places=0, verbose_name='Cantidad')
#     cant_process = models.DecimalField(default=0, max_digits=9, decimal_places=0, verbose_name='Cantidad en proceso')
#
#     def __str__(self):
#         return self.table
#
#     class Meta:
#         verbose_name = 'Venta'
#         verbose_name_plural = 'Ventas'
#         db_table = 'venta'
#         ordering = ['id']


# class Bill(models.Model):
#
#     sale = models.ForeignKey(Sale, on_delete=models.CASCADE, verbose_name="Venta")
#     prod = models.ForeignKey(Product, on_delete=models.CASCADE, verbose_name="Producto")
#     price = models.DecimalField(default=0.00, max_digits=9, decimal_places=2)
#     cant = models.IntegerField(default=0)
#     date = models.DateField(default=datetime.now, verbose_name='Fecha de venta')
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         verbose_name = 'Factura'
#         verbose_name_plural = 'Facturas'
#         db_table = 'factura'
#         ordering = ['id']
