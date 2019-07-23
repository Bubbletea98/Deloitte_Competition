from django.shortcuts import render
from .models import Post

# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #key
    }
    return render(request,'Education/home.html',context)

def about(request):
    return render(request,'Education/Map.html',{'title':'Map'})
