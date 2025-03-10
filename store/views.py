from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RegisterUser
from .forms import RegisterUserForm

def home(request):
    return render(
        request, 
        'store/home.html',
    )

def register(request):
    if request.method == 'POST':
        form = RegisterUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterUserForm()

    return render(
        request, 
        'store/register.html',
        {
            "form": form
        }
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

