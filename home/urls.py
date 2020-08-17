from django.contrib import admin
from django.urls import path, include
from . import views

admin.site.site_header = "iCoder Admin"
admin.site.site_title = "iCoder Admin Panel"
admin.site.index_title = "Welcome to iCoder Admin Panel"

urlpatterns = [
    path('', views.home, name='home'),
    path('contact', views.contact, name='contact'),
    path('about', views.about, name='about'),
    path('search', views.search, name='search'),
    path('signup', views.handleSignup, name='handleSignup'),
    path('login', views.handleLogin, name='handleLogin'),
    path('logout', views.handleLogout, name='handleLogout')
]