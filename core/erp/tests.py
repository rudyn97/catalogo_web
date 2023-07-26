from os import name

from cofig.wsgi import *
from core.erp.models import Category

#-----------------mostrar------------------
#select * from tabla
# obtener todo
#query = Type.objects.all()
#print(query)
#obtener todo
query = Category.objects.all()
print(query)
#obtener id especifico
#t = Type.objects.get(id=1)
#print(t.name)

#-----------------insercion------------------
#insercion 1
#t = Type()
#t.name = "PruebLLL"
#t.save()

#insercion 2
#t = Type(name="PruebLLL1")
#t.save()

#insercion 3
# t = Type(name="PruebLLL2").save()

#-------------------edicion----------------
#edicion (id o pk)
# t = Type.objects.get(id=1)
# t.name = "CAMBIADO"
# t.save()

#-------------------error ----------------
#edicion (id o pk)
# try:
#  t = Type.objects.get(id=1)
#  t.name = "CAMBIADO"
#  t.save()
# except Exception as e:
#     print(e)

#-----------------eliminacion------------------
# t = Type.objects.get(id=3)
# t.delete()

#####################################OTRAS FORMAS###############################################

#-----------------Listar filtrando palabra----------------------
# obj = Type.objects.filter(name__contains='Pru')
# print(obj)
#-----------------Listar filtrando palabra no importa mayuscula o minuscula----------------------
# obj = Type.objects.filter(name__contains='Pru')
# print(obj)
#-----------------Listar empieza con----------------------
# obj = Type.objects.filter(name__startswith='P')
# print(obj)
#-----------------Listar termina con----------------------
# obj = Type.objects.filter(name__endswith='O')
# print(obj)
#-----------------Listar entre----------------------
#obj = Type.objects.filter(name__in=['viva', 'hola'])
#-----------------Listar entre cantidad----------------------
#obj = Type.objects.filter(name__in=['viva', 'hola']).count()
#-----------------Codigo de la consulta----------------------
# obj = Type.objects.filter(name__contains='Pru').query
# print(obj)

#------------------------------------------------
#obj = Employee.objects.filter(type_id=1)

#for i in Type.objects.filter():
#    print(i.name)
