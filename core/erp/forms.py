from datetime import datetime

from django.core.mail.backends import console
from django.forms import ModelForm, TextInput, Textarea, forms, Form, ModelChoiceField, Select, DateInput

from core.erp.models import *


class CategoryForm(ModelForm):
    ####PARA GENERALIZAR DATOS(ESTOS COMPONENTES NO LOS TENGO QUE PONER DEBAJO)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
    #####

    class Meta:
        model = Category
        fields = '__all__'
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Escriba un nombre',
                }
            ),
            'desc': Textarea(
                attrs={
                    'placeholder': 'Escriba una descripcion',
                    'rows': 3,
                    'cols': 3
                }
            ),
        }
        exclude = ['user_updated', 'user_creation']

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data


class ProductForm(ModelForm):
    ####PARA GENERALIZAR DATOS(ESTOS COMPONENTES NO LOS TENGO QUE PONER DEBAJO)
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs['autofocus'] = True
    #####

    class Meta:
        model = Product
        fields = '__all__'
        #Personalizar el formulario pasandole atributos
        widgets = {
            'name': TextInput(
                attrs={
                    'placeholder': 'Escriba un nombre',
                }
            ),
            'cate': Select(
                attrs={
                    'class': 'select2',
                    'style': 'width: 100%'
                }
            ),
        }

    def save(self, commit=True):
        data = {}
        form = super()
        try:
            if form.is_valid():
                form.save()
            else:
                data['error'] = form.errors
        except Exception as e:
            data['error'] = str(e)
        return data

#
# class ClientForm(ModelForm):
#     def __int__(self, *args, **kwargs):
#         super().__int__(*args, **kwargs)
#         self.fields['names'].widget.attrs['autofocus'] = True
#
#     class Meta:
#         model = Client
#         fields = '__all__'
#         widgets = {
#             'name': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus nombres',
#                 }
#             ),
#             'surname': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese sus apellidos',
#                 }
#             ),
#             'dni': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su DNI',
#                 }
#             ),
#             'date_birthday': DateInput(
#                 format='%Y-%m-%d',
#                 attrs={
#                     'value': datetime.now().strftime('%Y-%m-%d'),
#                 }
#             ),
#             'address': TextInput(
#                 attrs={
#                     'placeholder': 'Ingrese su direccion',
#                 }
#             ),
#             'gender': Select()
#         }
#
#     def save(self, commit=True):
#         data = {}
#         form = super()
#         try:
#             if form.is_valid():
#                 form.save()
#             else:
#                 data['error'] = form.errors
#         except Exception as e:
#             data['error'] = str(e)
#         return data


class TestForm(Form):
    categories = ModelChoiceField(queryset=Category.objects.all(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'

    }))

    products = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))

    search = ModelChoiceField(queryset=Product.objects.none(), widget=Select(attrs={
        'class': 'form-control select2',
        'style': 'width: 100%'
    }))


