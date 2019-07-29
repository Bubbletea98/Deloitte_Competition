from django.shortcuts import render,get_object_or_404, redirect
from .models import Post, School, Student, Learning, Problem
from django.http import HttpResponseRedirect
from . import personalized_learning
from .form import NameForm, LearningForm
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

def addStudent(request):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student = Student()
            student.class_name = request.user.teacher.class_name
            student.name = form.cleaned_data.get('name')
            student.school = request.user.teacher.school
            student.save()
            return redirect('/students/')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return redirect('/students/')

# delete a student
def deleteStudent(request, pk):
    try:
        Student.objects.get(pk=pk).delete()
    except:
        return redirect('/students/')
    return redirect('/students/')

def studentDetail(request, pk):
    form = LearningForm()
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return redirect('/students/')
    context = {'student': student, 'user': request.user, 'title': 'student detail', 'form': form}
    return render(request,'Education/Management_detail.html',context)

def addLearning(request, pk):
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = LearningForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            student = Student.objects.get(pk=pk)
            learning_name = form.cleaned_data.get('name')
            correct = form.cleaned_data.get('score')
            difficulty = form.cleaned_data.get('difficulty')

            # check if this specific learning exists
            try:
                learning = student.learning_set.get(name=learning_name)
            except Learning.DoesNotExist:
                learning = Learning()
                learning.name = learning_name
                learning.student = student
                learning.save()
            
            # add a new problem
            problem = Problem(isCorrect=correct, learning=learning, difficulty=difficulty)
            learning.ability, learning.estimation = personalized_learning.updateAbility(learning,  [problem],list(learning.problem_set.all()))
            learning.save()
            problem.save()
            student.save()

            return redirect('/students/detail/{}'.format(pk))
        else:
            print(form.is_valid())

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()
        return redirect('/students/detail/{}'.format(pk))
