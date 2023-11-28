from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

# views.py

from django.shortcuts import render, redirect
from .forms import RegistrationForm,UserProfileForm

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('success')  # Redirect to a success page
    else:
        form = RegistrationForm()

    return render(request, 'register.html', {'form': form})

def home(request):
    return render(request,"index.html",{})
def ridepopup(request):
    return render(request,"ridepopup.html")
def soul(request):
    return render(request,"soul.html")
def soulreg(request):
    return render(request,"soulreg.html")
def gear(request):
    return render(request,"gear.html")
def fitzz(request):
    return render(request,"fitzz.html")
def spirit(request):
    return render(request,"spirit.html")
def cheackout(request):
    return render(request,"cheackout.html")
def bot(request):
    return render(request,"bot.html")

 #cheackout form

def cheackout_view(request):
    if request.method == 'POST':
        # Get form data from POST request
        name = request.POST.get('name')
        address = request.POST.get('address')
        email = request.POST.get('email')
        pincode = request.POST.get('pincode')
        phone = request.POST.get('phone')
        date = request.POST.get('date')
        time_slot = request.POST.get('time')

        checkout_instance = cheackout_view(
            name=name,
            address=address,
            email=email,
            pincode=pincode,
            phone=phone,
            date=date,
            time_slot=time_slot
        )
        checkout_instance.save()  # Use save() to persist the object to the database
        messages.success(request, 'Thank you,we will contact you soon!')
        return redirect('home')

    return render(request, 'cheackout.html')


# login form


# login view
def user_login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            # Add a message or handle the error
            messages.error(request, 'Invalid login credentials')
            return redirect('login')  # Consider redirecting to an error page or showing the login form with an error message
            
    return render(request, 'login.html')

# signup view
def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        my_user = User.objects.create_user(uname, email, password1)
        my_user.save()
        return redirect('login')
    
    return render(request, 'signup.html')  # Adjust the template name as needed

# register view
def register_view(request):
    if request.method == 'POST':
        form = UserProfileForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Thank you for registering!')
            return redirect('home')
    else:
        form = UserProfileForm()

    return render(request, 'register.html', {'form': form})






