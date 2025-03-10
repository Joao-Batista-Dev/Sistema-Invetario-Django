from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brand, Category, RegisterUser, RegisterProduct, Movement, Maintenance, EquipmentStatus
from django.contrib.auth import authenticate, login

def home(request):
    return render(
        request, 
        'store/home.html',
    )

def register(request):
    fullname = email = password = ""
    context = {}

    if request.method == 'POST':
        fullname = request.POST.get('fullname', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '').strip()
        

    if not (fullname and email and password):  
        context['erro'] = 'Preencha todos os campos!'
    elif RegisterUser.objects.filter(fullname=fullname, email=email).exists():
        context['erro'] = 'Usuário já cadastrado!'
    else:
        RegisterUser.objects.create(fullname=fullname, email=email, password=password)
        context['sucesso'] = 'Usuário cadastrado com sucesso!'

    return render(
        request, 
        'store/register.html',
        context
    )

def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        try:
            user = RegisterUser.objects.get(email=email)
        except RegisterUser.DoesNotExist:
            return render(
                request, 
                'store/login.html', 
            )

        if user.password == password:
             request.session['user_id'] = user.id
             return redirect('home')
        else:
            return render(
                request, 
                'store/login.html', 
                {'error': 'Senha incorreta!'}
            )
        
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

