from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import RegisterUser
from .forms import RegisterUserForm, LoginForm
from django.contrib.auth.hashers import check_password

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
    error_message = None

    if request.method == 'POST':
        form = LoginForm(request.POST)

        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            try:
                user = RegisterUser.objects.get(email=email)
                
                if user.password == password:  
                    request.session['user_id'] = user.id
                    request.session['user_fullname'] = user.fullname
                    request.session['user_email'] = user.email
                    
                    request.session.modified = True
                    
                    return redirect('home')
                else:
                    error_message = "Senha incorreta."

            except RegisterUser.DoesNotExist:
                error_message = "Usuário não encontrado."
    else:
        form = LoginForm()

    return render(
        request,
        'store/login.html',
        {
            'form': form, 
            'error_message': error_message
        }
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

