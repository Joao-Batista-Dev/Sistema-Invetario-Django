from django.shortcuts import render, redirect, get_object_or_404
from .models import RegisterUser, RegisterProduct
from .forms import RegisterUserForm, LoginForm

def home(request):
    qt_client = RegisterProduct.objects.count()
    equipments = RegisterProduct.objects.all()

    return render(
        request, 
        'store/home.html',
        {
            'qt_client': qt_client,
            'equipments': equipments,
        }
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
        "store/reports.html",
        {
            "reports": reports, 
            "form": form,
        }
    )

def equipment_registration(request):
    # get data forms
    if request.method == 'POST':
        name = request.POST.get('name')
        serial_number = request.POST.get('serial_number')
        date_aquisition = request.POST.get('date_aquisition')
        date_end = request.POST.get('date_end')
        leased = request.POST.get('leased')
        allocator = request.POST.get('allocator')
        address = request.POST.get('address')
        observations = request.POST.get('observations')

        # filter equipaments the sistem
        if RegisterProduct.objects.filter(serial_number=serial_number).exists():
            
            return render(
                request, 
                'store/equipment_registration.html', 
                {
                'error': 'Este número de série já está cadastrado.'
                }
            )

        # create equipament
        equipment = RegisterProduct(
            name=name,
            serial_number=serial_number,
            date_aquisition=date_aquisition,
            date_end=date_end,
            leased=leased,
            allocator=allocator,
            address=address,
            observations=observations
        )
        equipment.save()

        return redirect('equipment_registration') 

    # display all equipment
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
        equipment.serial_number = request.POST.get("serial_number")
        equipment.date_aquisition = request.POST.get("date_aquisition")
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