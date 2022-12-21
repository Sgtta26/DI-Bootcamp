from django.shortcuts import render, redirect
from django.contrib import messages, auth
from django.contrib.auth.models import User


# Create your views here.
def register(request):
    if request.method == "POST":
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request. POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
        # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register') 
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used') 
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                    username=username,
                    password=password,
                    email=email, 
                    first_name=first_name, 
                    last_name=last_name
                    )
                    user.save()
                    messages.success(request, 'you are registered and can login')
                    return redirect('login')
        else:
            messages.error(request, 'password not matched')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')

def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
         
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user) 
            messages.success(request, 'you are now Logged in!')
            return redirect('dashboard')
        else:
            messages.error(request, 'INVALID CREDENTIALS, try again...')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')

def dashboard(request):
    user_contacts = Contact.objects.order_by('-contact date').filter(user_id=request.user.id)
    context = {
        'contacts': user_contacts
    }
    return render(request, 'accounts/dashboard.html')

def logout(request):
    if request.method == "POST":
        auth.logout(request)
        messages.success(request, 'you are logged out')
        return redirect('index')
