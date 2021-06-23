from django.urls import path
from core.views import *
urlpatterns = [
    path('', home, name='home'),
    path('listar/', ListarCanciones, name='listar'),
    path('agregar/', CrearCancion, name="agregar"),
    path('eliminar/<int:id_cancion>/', EliminarCancion, name='eliminar'),
    path('editar/<int:id_cancion>/', EditarCancion, name='editar'),
    path('info/<int:id_cancion>/', VerInfor, name='informacion'),
]