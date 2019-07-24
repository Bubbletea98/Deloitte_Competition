from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm
from django.contrib.auth.models import User
from Education.models import Teacher
from Education.models import School

def register (request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            user = User.objects.get(username = username)
            teacher = Teacher(name = username)
            teacher.school = School.objects.get(pk=1)
            teacher.user = user
            teacher.save()
            return redirect('home-page')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile (request):
    return render (request,'users/profile.html')


# Create your views here.
