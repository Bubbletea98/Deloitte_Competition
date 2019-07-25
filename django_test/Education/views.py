from django.shortcuts import render
from .models import Post
from .models import School

mapbox_access_token = 'Please find your location'
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #key
    }
    return render(request,'Education/home.html',context)

def about(request):
	schools = School.objects.all()
	return render(request,'Education/Map.html',
    	{'title':'Map',
    	'schools': schools})
