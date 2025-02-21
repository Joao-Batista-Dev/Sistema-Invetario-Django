from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name='login'),
    path('cadastro/', views.register, name='register'),
    path('home/', views.home, name='home'), 
    path('relatorios/', views.reports, name='reports'),
    path('controle_de_saida_e_entrada/', views.entry_and_exit_control, name='entry_and_exit_control'),
    path('manutencao_equipamento/', views.equipment_maintenance, name='equipment_maintenance'),
    path('registro_equipamento/', views.equipment_registration, name='equipment_registration'),
    path('status_do_equipamento/', views.equipment_status, name='equipment_status'),
]
