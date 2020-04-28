from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def home(request):
    request.session.clear()
    return redirect('/main')
def main(request):
    if 'user' not in request.session:
        request.session['user']={}
    return render(request,'main.html')
def register(request):
    print(request.POST)
    errors= User.objects.reg_validation(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v,extra_tags=k)
        return redirect('/')
    else:
        a=request.POST['name']
        b=request.POST['username']
        c=request.POST['password']
        d=request.POST['r_password']
        hashedpw= bcrypt.hashpw(c.encode(),bcrypt.gensalt()).decode()
        User.objects.create(name=a, username=b, password=hashedpw)
        new_user=User.objects.get(username=b)
        request.session['user']={
            'name': new_user.name,
            'id': new_user.id
        }
        return redirect('/')
def login (request):
    errors= User.objects.log_validation(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v,extra_tags=f'{k}')
        return redirect('/')
    else:
        a=request.POST['l_username']
        selected_user= User.objects.get(username=a)
        request.session['user']={
            'name': selected_user.name,
            'id': selected_user.id
        }
        return redirect('/travels')
# Create your views here.
