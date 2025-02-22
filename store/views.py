from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(
        request, 
        'store/home.html',
        context= {'name': 'teste'},
    )

def register(request):
    return render(
        request, 
        'store/register.html',
    )

def login(request):
    return render(
        request,
        'store/login.html',
    )

def reports(request):
    return render(
        request,
        'store/reports.html',
    )

def entry_and_exit_control(request):
    return render(
        request,
        'store/entry_and_exit_control.html'
    )

def equipment_maintenance(request):
    return render(
        request,
        'store/equipment_maintenance.html'
    )

def equipment_registration(request):
    return render(
        request,
        'store/equipment_registration.html'
    )

def equipment_status(request):
    return render(
        request,
        'store/equipment_status.html'
    )

