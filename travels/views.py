from django.shortcuts import render, redirect
from .models import Plan
from login_registration.models import User
from django.contrib import messages
# Create your views here.
def dashboard(request):
    if 'user' not in request.session: 
        return redirect('/')
    else:
        a=request.session['user']
        selected_user=User.objects.get(id=a['id'])
        print(selected_user)
        context={
            'user_plans': selected_user.joined.all(),
            'other_plans': Plan.objects.exclude(creator=selected_user).exclude( passengers=selected_user).all()
        }
        print(context)
    return render (request,'dashboard.html',context)
def add_plan(request):
    if 'user' not in request.session: 
        return redirect('/')
    else:
        return render(request,'add_plan.html')
def adding_plan(request):
    errors= Plan.objects.plan_validation(request.POST)
    if errors:
        for k,v in errors.items():
            messages.error(request,v,extra_tags=f'{k}')
        return redirect('/travels/add')
    else:
        a=request.POST['destination']
        b=request.POST['desc']
        c=request.POST['date_start']
        d=request.POST['date_end']
        e=request.POST['user_id']
        creator=User.objects.get(id=e)
        Plan.objects.create(creator=creator,destination=a,desc=b,date_start=c,date_end=d)
        new_plan=Plan.objects.get(creator=creator,destination=a,desc=b,date_start=c,date_end=d)
        new_plan.passengers.add(creator)
        return redirect('/travels')
def plan_details(request,id):
    selected_plan=Plan.objects.get(id=int(id))
    context={
        'plan': selected_plan,
    }
    return render(request,'plan_details.html',context)
def join_plan(request,id):
    a=request.session['user']
    user=User.objects.get(id=a['id'])
    selected_plan=Plan.objects.get(id=int(id))  
    selected_plan.passengers.add(user)
    return redirect ('/travels')
