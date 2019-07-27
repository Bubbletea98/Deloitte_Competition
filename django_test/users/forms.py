from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Profile

class UserRegisterForm (UserCreationForm) :
    email = forms.EmailField()

    name = forms.CharField(
        label = "真实姓名",
        max_length = 80,
        required = True,
    )
    school_name = forms.CharField(
        label = "学校名称",
        max_length = 80,
        required = True,
    )

    school_address = forms.CharField(
        label = "学校地址",
        max_length = 80,
        required = False,
    )

    class_name = forms.CharField(
        label = "班级名称",
        max_length = 80,
        required = True,
    )


    class Meta :
        model =User
        fields =['username','email','password1','password2', 'name', 'school_name', 'school_address','class_name']

class UserUpdateForm(forms.ModelForm):
    email =forms.EmailField()

    class Meta:
        model =User
        fields =['username','email']


class ProfileUpdateForm(forms.ModelForm):
    class Meta:
        model= Profile
        fields =['image']
