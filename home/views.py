from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.views.generic import TemplateView
from datetime import datetime
from django.contrib.auth.mixins import LoginRequiredMixin
# Create your views here.

# def home(request):
#     return render(request,'home/welcome.html',{})

class HomeView(TemplateView):
    template_name = 'home/welcome.html'
    extra_context ={'today':datetime.now()}

# @login_required(login_url='/admin')
# def authorize(request):
#     return render(request,'home/authorized.html',{})
    

class AuthorizedView(LoginRequiredMixin,TemplateView):
    template_name = 'home/authorized.html'
    login_url = '/admin'

