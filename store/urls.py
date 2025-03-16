from django.urls import path
from . import views


urlpatterns = [
    path('', views.login, name='login'),
    path('home/', views.home, name='home'),
    path('cadastro/', views.register, name='register'),
    path('relatorios/', views.reports, name='reports'),
    path('controle-de-saida-e-entrada/', views.entry_and_exit_control, name='entry_and_exit_control'),
    path('manutencao-equipamento/', views.equipment_maintenance, name='equipment_maintenance'),
    path('registro-equipamento/', views.equipment_registration, name='equipment_registration'),
    path('status-do-equipamento/', views.equipment_status, name='equipment_status'),
    path('excluir-equipamento/<int:id>/', views.delete_equipment, name='delete_equipment'),
    path('equipments/edit/<int:id>/', views.edit_equipment, name='edit_equipment'),
]
