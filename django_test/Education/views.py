from django.shortcuts import render,get_object_or_404
from .models import Post
from .models import School
from .models import Student
from django.http import HttpResponseRedirect
from .form import NameForm
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.contrib.auth.models import User
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

class UserPostListView(ListView):
    model =Post
    template_name = 'Education/user_posts.html' #<app>/<model>_<viewtype>.html
    context_object_name ='posts'
    ordering =['-date_posted'] #from latest to oldest
    def get_query_set(self):
        user= get_object_or_404(User, username=self.kwargs.get('username'))
        return Post.objects.filter(Teacher=user).order_by('-date_posted')

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
    form = NameForm()
    return render(request,'Education/studentManagement.html',
    	{'title':'studentManagement',
    	'user': request.user,
        'form': form})

def Management_detail(request):
    print(request.user)
    return render(request,'Education/Management_detail.html',
           {'title':'Management_detail',
           'user': request.user})

def addStudent(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student = Student()
            student.class_name = request.user.teacher.class_name
            student.name = form.your_name
            student.school = request.user.teacher.name
            student.save()
            return HttpResponseRedirect('/students/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return HttpResponseRedirect('/students/')
