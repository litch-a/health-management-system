from django.shortcuts import render, redirect
from django.http import JsonResponse, Http404
from .forms import ClientForm, HealthProgramForm, ClientEnrollmentForm
from .models import Client, HealthProgram


def dashboard_content(request):
   client = Client.objects.first()
   return render(request, 'dashboard.html', {'client': client})

#View for Registering a Client
def register_client_content(request):
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Client registered successfully!'})
            else:
                return redirect('dashboard')  # fallback
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'message': 'Form validation failed.', 'errors': errors})
    else:
        form = ClientForm()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/register_client.html', {'form': form})
    
    return render(request, 'dashboard.html', {'form': form})

# View for Creating a Health Program
def create_health_program_content(request):
    if request.method == 'POST':
        form = HealthProgramForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Health program created successfully!'})
            else:
                # fallback if normal POST
                return redirect('health_programs_list')  
        else:
            print(form.errors) #This will print form validation errors in the server logs
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                # collect form errors
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'message': 'Form validation failed.', 'errors': errors})
    else:
        form = HealthProgramForm()
    
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/create_health_program.html', {'form': form})
    else:
        return render(request, 'health_programs/create_health_program.html', {'form': form})

# View for Viewing Clients
def clients_list_content(request):
    clients = Client.objects.all()
    return render(request, 'partials/clients_list.html', {'clients': clients})


# View for Viewing Health Programs
def health_programs_list_content(request):
    programs = HealthProgram.objects.all()
    return render(request, 'partials/health_programs_list.html', {'programs': programs})

# View for Enrolling a Client
def enroll_client_content(request):
    if request.method == "POST":
        form = ClientEnrollmentForm(request.POST)
        if form.is_valid():
            form.save()
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                return JsonResponse({'success': True, 'message': 'Client enrolled successfully!'})
            else:
                return redirect('health_app:clients_list_content')
        else:
            if request.headers.get('x-requested-with') == 'XMLHttpRequest':
                errors = form.errors.as_json()
                return JsonResponse({'success': False, 'message': 'Form validation failed.', 'errors': errors})
    else:
        form = ClientEnrollmentForm()

    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        return render(request, 'partials/enroll_client.html', {'form': form})
    
    return render(request, 'dashboard.html', {'form': form})

