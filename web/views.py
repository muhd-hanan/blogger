from django.shortcuts import render, redirect

from django.contrib.auth import authenticate ,login as auth_login ,logout
from django.contrib.auth.models import User
from .models import Author
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'index.html')


def create(request):
    return render(request, 'create.html')

def account(request):
    return render(request, 'account.html')

def blog(request):
    return render(request, 'blog.html')

def register(request):

    if request.method =='POST':
        username = request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        password = request.POST.get('password')

        if User.objects.filter(username=username).exists():
            return render(request, 'register.html', {'errors': 'Username already exists'})
        else:
            user = User.objects.create_user(
                username=username,  
                first_name=first_name,
                last_name=last_name,
                password=password
            )        

        author = Author.objects.create(
            user=user
        )
        return redirect('web:login')


    else:
        return render(request, 'register.html')

def login(request):

    if request.method == 'POST':
        username = request.POST.get('username') 
        password = request.POST.get('password')
        if username and password:
            user = authenticate(request, username=username, password=password)
            if user:
                auth_login(request,user)
                return redirect('web:index')
            else:
                 return render(request, 'login.html', {'error': 'Invalid username or password'})
        else:
            return render(request, 'login.html')

    else:

        return render(request, 'login.html')

def logout(request):
    pass
    return render(request, 'logout.html')





