from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('eventos/', views.lista_eventos, name='lista_eventos'),
    path('eventos/crear/', views.crear_evento, name='crear_evento'),
    path('eventos/editar/<int:id>/', views.editar_evento, name='editar_evento'),
    path('eventos/eliminar/<int:id>/', views.eliminar_evento, name='eliminar_evento'),

    path('participantes/', views.lista_participantes, name='lista_participantes'),
    path('participantes/crear/', views.crear_participante, name='crear_participante'),
    path('participantes/editar/<int:id>/', views.editar_participante, name='editar_participante'),
    path('participantes/eliminar/<int:id>/', views.eliminar_participante, name='eliminar_participante'),
]

