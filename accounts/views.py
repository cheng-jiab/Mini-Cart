from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages, auth


# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            firstName = form.cleaned_data['firstName']
            lastName = form.cleaned_data['lastName']
            phoneNumber = form.cleaned_data['phoneNumber']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split("@")[0]
            user = Account.objects.create_user(
                firstName=firstName, 
                lastName=lastName, 
                email=email, 
                username=username, 
                password=password)
            user.phoneNumber = phoneNumber
            user.save()
            messages.success(request, 'Registration Successful')
            return redirect('register')

    else:
        form = RegistrationForm()

    context = {
        'form': form,
    }
    return render(request, 'accounts/register.html', context)

def login(request):
    if request.method == "POST":
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)
        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            return redirect('home')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')

def logout(request):
    return 