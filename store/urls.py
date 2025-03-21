from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.register, name='register'),
    path('relatorios/', views.reports, name='reports'),
    path('registro-equipamento/', views.equipment_registration, name='equipment_registration'),
    path('excluir-equipamento/<int:id>/', views.delete_equipment, name='delete_equipment'),
    path('equipamento/editar/<int:id>/', views.edit_equipment, name='edit_equipment'),
]
