from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from Education.models import Teacher
from Education.models import School
from Education.models import Class



def register (request):
    if request.method =='POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username= form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            user = User.objects.get(username = username)
            name = form.cleaned_data.get('name')
            school_name = form.cleaned_data.get('school_name')
            school_address = form.cleaned_data.get('school_address')
            class_name = form.cleaned_data.get('class_name')
            latitude = form.cleaned_data.get('lat')
            longitude = form.cleaned_data.get('longi')
            teacher = Teacher(name = name)
            schools = list(School.objects.filter(name=school_name, address=school_address))
            if(len(schools) > 0):
                teacher.school = schools[0]
                school = schools[0]
            else:
                school = School(name=school_name, address=school_address, latitude=latitude, longitude=longitude)
                school.save()
                teacher.school = school
            
            classes = school.class_set.filter(name=class_name)
            if(len(classes) > 0):
                teacher.class_name = classes[0]
            else:
                cl = Class(name=class_name)
                cl.school = school
                cl.save()
                teacher.class_name = cl
            teacher.user = user
            teacher.save()
            return redirect('home-page')
    else:
        form = UserRegisterForm()
    return render(request,'users/register.html',{'form':form})

@login_required
def profile (request):
    if request.method =='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)

        if u_form.is_valid()and p_form.is_valid():
            u_form.save()
            p_form.save()
            messages.success(request,f'Your account has been updated!')
            return redirect('profile')
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)

    context={
        'u_form': u_form,
        'p_form':p_form
    }
    return render (request,'users/profile.html',context)


# Create your views here.
