from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth.models import User , auth

def index(request):
    return render(request,'index.html')

def sign_in(request):
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('password')

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            messages.info(request,'Login Successfully')
            return redirect('profile')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('sign_in')
    else:
       return render(request,'sign_in/sign_in.html')

def sign_up(request):
    if request.method== 'POST':
        print('username')
        if request.POST['first_name'] and request.POST['last_name'] and request.POST['email'] and request.POST['password']:
            email=request.POST['email']
            password=request.POST['password']
            first_name=request.POST['first_name']
            last_name=request.POST['last_name']
            password1=request.POST['retype_pass']
            if password==password1:
                if User.objects.filter(username=email).exists():
                    messages.info(request,'username already taken.')
                    return redirect('sign_up')
                elif User.objects.filter(email=email).exists():
                    messages.info(request,'email already taken..')
                    return redirect('sign_up')
                else:
                    user=User.objects.create_user(username=email,password=password,email=email,first_name=first_name,last_name=last_name)
                    user.save()
                    messages.info(request,'User created successfully.')
                return redirect('sign_in')
            else:
                messages.info(request,'password not matching, please try again')
                return redirect('sign_up')
        else :
            messages.info(request,'Please make sure all required fields are filled out correctly')
            return redirect('sign_up')
    else:   
        return render(request,'sign_up/sign_up.html')

def profile(request):
    return render(request,'profile/profile.html')