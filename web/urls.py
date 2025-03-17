from django.urls import path 
from . import views


app_name = 'web'
urlpatterns = [

    path('',views.index,name='index'),
    path('create/', views.create, name='create'),
    path('account/', views.account, name='account'),
    path('blog/<int:id>/', views.blog, name='blog'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('logout/', views.logout, name='logout'),
    path('delete/<int:id>/', views.delete, name='delete'),
    path('edit/<int:id>/', views.edit, name='edit'),


        

]