from django.shortcuts import render

# Create your views here.
from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from .forms import CustomerCreationForm
from django.views import View
from django.contrib import messages

def home(request):
    return render(request, 'shop/home.html')

class SignUp(View):
    def get(self, request):
        form = CustomerCreationForm()
        return render(request, 'shop/signup.html', {'form':form})
    def post(self, request):
        form = CustomerCreationForm(request.POST)
        if form.is_valid():
            messages.success(request, 'Congraglations you did sighnup porfictly')
            form.save()
            return render(request, 'shop/signup.html', {'form':form})

    
def shopPage(request):
    return render(request, 'shop/shopPage.html')

def about(request):
    return render(request, 'shop/about.html')

def contact(request):
    return render(request, 'shop/contact.html')

def tracker(request):
    return render(request, 'shop/tracker.html')

def searchMatch():
    pass
def search(request):
    return render(request, 'shop/search.html')
def productView(request):
    return render(request, 'shop/productView.html')

def checkout(request):
    return render(request, 'shop/checkout.html')




def LoginPage(request):
   
    return render(request, 'shop/login.html')


def error(request):
    return render(request, 'shop/password_incorrect.html')

def error2(request):
    return render(request, 'shop/password_incorrect2.html')

def LogoUt(request):
    return render(request,'shop/logoutPage.html')

def Logout(request):
    logout(request)
    return redirect('homePAGE')