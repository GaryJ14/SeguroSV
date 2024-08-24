from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index),
    path('login', views.login,name='login'),
    path('registro', views.registro,name='registro'),
    path('guardarRegistro', views.guardarRegistro, name='guardarRegistro'),
    path('menu', views.menu,name='menu'),
    path('empresa', views.empresa,name='empresa'),
    path('cliente', views.cliente,name='cliente'),
    path('seguimiento', views.seguimiento,name='seguimiento'),
    path('postventa', views.postventa,name='postventa'),
    path('guardar_cliente', views.guardar_cliente,name='guardar_cliente'),
    path('guardarEmpresa', views.guardarEmpresa,name='guardarEmpresa'),
    path('guardarPostventa', views.guardarPostventa,name='guardarPostventa'),
    path('agregarSeguimiento', views.agregarSeguimiento,name='agregarSeguimiento'),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)