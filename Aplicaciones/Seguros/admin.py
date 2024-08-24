from django.contrib import admin
from .models import Registro, Cliente,Empresa,PostVenta,Seguimiento
# Register your models here.
admin.site.register(Registro)
admin.site.register(Cliente)
admin.site.register(Empresa)
admin.site.register(PostVenta)
admin.site.register(Seguimiento)