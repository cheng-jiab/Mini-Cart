from django.contrib.sites import requests
from accounts.forms import RegistrationForm
from django.shortcuts import render, redirect
from .models import Account
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# Verification email
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes
from django.contrib.auth.tokens import default_token_generator
from django.core.mail import EmailMessage
from carts.views import _cartId
from carts.models import Cart, CartItem

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

            # user activation
            currentSite = get_current_site(request)
            mailSubject = "Please active your account"
            message = render_to_string('accounts/verificationEmail.html', {
                'user': user,
                'domain': currentSite,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user)

            } )
            toEmail = email
            sendEmail = EmailMessage(mailSubject, message, to=[toEmail])
            sendEmail.send()

            messages.success(request, 'Thank you for registering, we have sent you a verificcation email to your mailbox. Please verify it.')
            return redirect('/accounts/login/?command=verification&email='+email)

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
            # check user's cart items
            try:
                cart = Cart.objects.get(cartId = _cartId(request))
                if CartItem.objects.filter(cart=cart).exists():
                    cartItems = CartItem.objects.filter(cart=cart)
                    for item in cartItems:
                        item.user = user
                        item.save()
            except:
                pass
            auth.login(request, user)
            messages.success(request, 'You are now logged in.')
            

            return redirect('store')
        else:
            messages.error(request, "Invalid login credentials")
            return redirect('login')

    return render(request, 'accounts/login.html')

@login_required(login_url = 'login')
def logout(request):
    auth.logout(request)
    messages.success(request, 'You are logged out.')
    return redirect('login')

def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, 'Congratulations! Your account is activated')
        return redirect('login')
    else:
        messages.error(request, 'Invalid activaation Link')
        return redirect('register')

@login_required(login_url='login')
def dashboard(request):
    # TODO: User dashborad
    #return render(request, 'accounts/dashboard.html')
    return HttpResponse('Sorry, it is still in progress')


def forgotPassword(request):
    if request.method == "POST":
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact=email)

            # resend verification email
            currentSite = get_current_site(request)
            mailSubject = "Reset your password"
            message = render_to_string('accounts/resetPasswordEmail.html', {
                'user': user,
                'domain': currentSite,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),

            } )
            toEmail = email
            sendEmail = EmailMessage(mailSubject, message, to=[toEmail])
            sendEmail.send()

            messages.success(request, 'Reset Email Has Been Sent!')
            return redirect('login')

        else:
            messages.error(request, "Account Does Not Exist") 
            return redirect('forgotPassword')

    return render(request, 'accounts/forgotPassword.html')


def resetPassword(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)

    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None

    if user and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request, 'Please rest your password')
        return redirect('resetPasswordPage')

    else:
        messages.error(request, "This link has been expired")
        return redirect('login')

def resetPasswordPage(request):
    if request.method == "POST":
        password = request.POST['password']
        confirmPassword = request.POST['confirmPassword']
        if password == confirmPassword:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successful')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match')
            return redirect('resetPassword')

    else:
        return render(request, 'accounts/resetPassword.html')