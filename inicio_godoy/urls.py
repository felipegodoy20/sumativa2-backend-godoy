from django.urls import path
from . import views

app_name = 'inicio_godoy'
urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('tema/<int:tema_id>/', views.detalle_tema, name='detalle_tema'),
]