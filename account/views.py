from django.contrib import auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model,authenticate

from django.contrib.auth.hashers import make_password,check_password
from django.contrib.messages.storage import session
from django.db.models import Q
from django.shortcuts import render, redirect
from listings.models import OrderBooking
from django.contrib import messages

from django.http import HttpResponse


# Create your views here.



def login(request):
    if request.method=='POST':
        username = request.POST['username']#user@gmail.com
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            #messages.success(request,'you are now logged in')
            auth.login(request,user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        # messages.error(request, 'Invalid credentials')
        return render(request,'account/login.html')


def register(request):
    if request.method == 'POST':
        UserModel = get_user_model()
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # check if password match

        if password == password2:
            # check username
            password=make_password(password)
            if UserModel.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                # check email exist
                if UserModel.objects.filter(email=email).exists():
                    messages.error(request, 'That email is taken')
                    return redirect('register')
                else:
                    user = UserModel.objects.create(username=username, email=email, password=password)
                    user.save()
                    messages.success(request, 'you are now logged in')
                    return redirect('login')
        else:
            messages.error(request, 'password do not match')
            return redirect('register')
        #messages.success(request,'you are now login')
    return render(request,'account/register.html')


def dashboard(request):
    booked_list=OrderBooking.objects.order_by('-order_date').filter(user_id=request.user.id)
    context={
        'booked_list':booked_list
    }
    return render(request,'account/dashboard.html',context)


def logout(request):
    auth.logout(request)
    return redirect('index')