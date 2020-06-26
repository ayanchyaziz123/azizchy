from django.http import HttpResponse
from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from .models import Account
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from .forms import RegistrationForm
from home.models import Category, Post


# Create your views here.


def userSignUp(request):
    context = {}
    Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
    cat = Category.objects.all()[0:3]

    
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_password = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_password)
            login(request, account)
            return redirect('home')
        else:
            context['registration_form'] = form
    else:  # GET request
        form = RegistrationForm()
        Recent = Post.objects.all().order_by('-postTimeDate')[0:4]
        cat = Category.objects.all()[0:3]
        context  = {'registration_form' : form,
                'RecentPost': Recent,
                   'Categories': cat,}
    return render(request, 'SignUp.html', context)




def userProfile(request):
    return render(request, 'user/userProfile.html')


def userLogIn(request):
    if request.method == 'POST':
        em = request.POST['email']
        pas = request.POST['pass']
        user = authenticate(email=em, password=pas)
        if user is not None:
            login(request, user)
            messages.success(request, 'successfully logged in')
            return redirect('home')
        else:
            messages.error(request, 'not logged in')
            return redirect('home')

    return HttpResponse('404 error page not found')


def userLogOut(request):
    logout(request)
    messages.success(request, 'successfully logged out')
    return redirect('home')
