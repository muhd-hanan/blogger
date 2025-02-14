from django.shortcuts import render, redirect, reverse
from web.models import Category ,Tag,Author, Blog
from django.contrib.auth import authenticate ,login as auth_login ,logout as auth_logout
from django.contrib.auth.models import User
from .models import Author
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponseRedirect

# Create your views here.

@login_required(login_url='login/')
def index(request):
    category = Category.objects.all()
    tag = Tag.objects.all()
    author = Author.objects.all()
    blog = Blog.objects.all()


    
    

    context = {
        'category': category,
        'tag': tag,
        'author': author,
        'blog': blog,
    

        
    }
    return render(request, 'index.html',context=context)
    

@login_required(login_url='login/')
def create(request):
    return render(request, 'create.html')
@login_required(login_url='login/')
def account(request):
    return render(request, 'account.html')
@login_required(login_url='login/')
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

@login_required(login_url='login/')
def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('web:login'))





