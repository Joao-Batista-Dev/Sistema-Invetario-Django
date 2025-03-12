from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .models import RegisterUser, RegisterProduct
from .forms import RegisterUserForm, LoginForm

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
    if request.method == 'POST':
        name = request.POST.get('name')
        type = request.POST.get('type')
        serial_number = request.POST.get('serial_number')
        date_aquisition = request.POST.get('date_aquisition')
        status_product = request.POST.get('status_product')
        supplier = request.POST.get('supplier')
        observations = request.POST.get('observations')

        if RegisterProduct.objects.filter(serial_number=serial_number).exists():
            
            return render(
                request, 
                'store/equipment_registration.html', 
                {
                'error': 'Este número de série já está cadastrado.'
                }
            )

        # Criação do novo equipamento
        equipment = RegisterProduct(
            name=name,
            type=type,
            serial_number=serial_number,
            date_aquisition=date_aquisition,
            status_product=status_product,
            supplier=supplier,
            observations=observations
        )
        equipment.save()

        return redirect('equipment_registration')  # Redireciona após o cadastro

    # Recupera todos os equipamentos para exibir na página
    equipment = RegisterProduct.objects.all()

    return render(
        request,
        'store/equipment_registration.html',
        {
            'equipment': equipment
        }
    )

def delete_equipment(request, id):
    equipment = get_object_or_404(RegisterProduct, id=id)
    equipment.delete()

    return redirect('equipment_registration')

def edit_equipment(request, id):
    equipment = get_object_or_404(RegisterProduct, id=id)

    if request.method == "POST":
        equipment.name = request.POST.get("name")
        equipment.type = request.POST.get("type")
        equipment.serial_number = request.POST.get("serial_number")
        equipment.date_aquisition = request.POST.get("date_aquisition")
        equipment.status_product = request.POST.get("status_product")
        equipment.supplier = request.POST.get("supplier")
        equipment.observations = request.POST.get("observations")
        
        equipment.save()
        return redirect("equipment_list") 

    return render(
        request, 
        "store/edit_equipment.html", 
        {
            "equipment": equipment
        }
    )

def equipment_status(request):
    return render(
        request,
        'store/equipment_status.html'
    )

