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
    user = request.user
    author = Author.objects.get(user=user)
    blog = Blog.objects.filter(author=author)  

    context = {
        'author': author,
        'blog': blog,
              
    }

    return render(request, 'account.html',context=context)

def delete(request, id):
    blog = Blog.objects.get(id=id)
   
    blog.delete()
    return redirect('web:index')

@login_required(login_url='login/')
def blog(request,id):
    blog = Blog.objects.get(id=id)
    context = {
        'blog': blog
    }

    return render(request, 'blog.html', context=context)

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
    return redirect(reverse('web:login'))


@login_required(login_url='login/')
def create(request):
    user = request.user
    author = Author.objects.get(user=user)
    categories = Category.objects.all()
    
    if request.method == 'POST':
        heading = request.POST.get('title') 
        image = request.FILES.get('image')  
        mini_content = request.POST.get('description')  
        category_id = request.POST.get('category')
        content = request.POST.get('description_big')  

        

       
        blog = Blog.objects.create(
            heading=heading,
            image=image,
            mini_content=mini_content,
            category_id=category_id,
            content=content,
            author=author,
        )
        
        return redirect('web:index')
    
    else:        
        return render(request, 'create.html', {'categories': categories})


@login_required(login_url='login/')
def edit(request,id):
   
   
    categories = Category.objects.all()
    blog = Blog.objects.get(id=id)
    
    if request.method == 'POST':
        heading = request.POST.get('title') 
        image = request.FILES.get('image')  
        mini_content = request.POST.get('description')  
        category_id = request.POST.get('category')
        content = request.POST.get('description_big')  

        

       
        blog = Blog.objects.create(
            heading=heading,
            image=image,
            mini_content=mini_content,
            category=category_id,
            content=content,
            
        )
        
        return redirect('web:index')
    
    else:        
        return render(request, 'create.html', {'categories': categories})
    

@login_required(login_url='login/')
def edit(request, id):
    blog = Blog.objects.get(id=id)  
    categories = Category.objects.all()  
    
    if request.method == 'POST':
        blog.heading = request.POST.get('title')  
        blog.mini_content = request.POST.get('description')  
        blog.category_id = request.POST.get('category') 
        blog.content = request.POST.get('description_big')  

        if request.FILES.get('image'): 
            blog.image = request.FILES.get('image')  

        blog.save()  
        
        return redirect('web:account')  
    

    return render(request, 'create.html', {'blog': blog, 'categories': categories})

