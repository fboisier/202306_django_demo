from django.urls import path     
from . import views

# /

urlpatterns = [
    path('correo', views.index),	   
    path('usuario/<int:user_id>', views.user_id),	   
    path('usuario/<str:nombre>/<str:apellido>', views.nombre),	   
    path('inicio', views.inicio),	   
    path('permisos', views.Permisos.as_view()),	   
    path('formulario', views.some_function),
    path('procesar_datos_kanskansjanskasnkans', views.procesar_datos, name="procesar"),
    path('plataformas', views.plataformas, name="plataformas"),
]