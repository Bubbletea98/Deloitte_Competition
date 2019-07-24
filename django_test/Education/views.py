from django.shortcuts import render
from .models import Post
mapbox_access_token = 'pk.eyJ1IjoicTUzNjc3NjEwIiwiYSI6ImNqeWdvZnk3NjAzOG0zYm8wbWcycXJ6ZmsifQ.qJRHm8_RkqqT5rc-EaFW6g'
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #key
    }
    return render(request,'Education/home.html',context)

def about(request):
    return render(request,'Education/Map.html',{
    	'title':'Map',
    	'mapbox_access_token': mapbox_access_token})
