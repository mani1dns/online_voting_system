from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegistrationForm
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    return render(request, 'login.html')

def register(request):
    if request.method == "POST":
        form = RegistrationForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            if cd['password'] == cd['confirm_password']:
                obj = form.save(commit=False)
                obj.set_password(obj.password)
                obj.save()
                form.save()
                messages.success(request, 'You have been registered successfully.')
                return redirect('index')
                return render(request, 'index.html')
            else:
                return render(request, "register.html", {'form':form,'note':'password must match'})
    else:
        form = RegistrationForm()

    return render(request, "register.html", {'form':form})
    