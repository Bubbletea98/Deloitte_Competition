from django.shortcuts import render
from .models import Post
from .models import School
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import (
ListView,
DetailView,
CreateView,
UpdateView,
DeleteView
)


mapbox_access_token = 'Please find your location'
# Create your views here.
def home(request):
    context = {
        'posts': Post.objects.all() #key
    }
    return render(request,'Education/home.html',context)

class PostListView(ListView):
    model=Post
    template_name = 'Education/home.html' #<app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering =['-date_posted'] #from latest to oldest

class PostDetailView(DetailView):
    model = Post

class PostCreateView(LoginRequiredMixin,CreateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.Teacher = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin,UserPassesTestMixin,UpdateView):
    model = Post
    fields=['title','content']

    def form_valid(self,form):
        form.instance.Teacher = self.request.user
        return super().form_valid(form)

    def test_func(self):
        post=self.get_object()
        if self.request.user == post.Teacher:
            return True
        return False

class PostDeleteView(LoginRequiredMixin,UserPassesTestMixin,DeleteView):
    model = Post
    success_url='/'
    def test_func(self):
        post=self.get_object()
        if self.request.user == post.Teacher:
            return True
        return False


def about(request):
	schools = School.objects.all()
	return render(request,'Education/Map.html',
    	{'title':'Map',
    	'schools': schools})

def studentManagement(request):
    print(request.user)
    return render(request,'Education/studentManagement.html',
    	{'title':'studentManagement',
    	'user': request.user})

def Management_detail(request):
    print(request.user)
    return render(request,'Education/Management_detail.html',
           {'title':'Management_detail',
           'user': request.user})
