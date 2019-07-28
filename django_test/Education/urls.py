from django.urls import path
from . import views
from .views import (
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView,
  UserPostListView
  )
urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('user/<str:username>', UserPostListView.as_view(), name='user-posts'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('Map/', views.about, name='home-map'),
    path('students/', views.studentManagement, name='student-management'),
    path('students/update/',views.addStudent, name='add_student'),
    path('students/delete/<int:pk>', views.deleteStudent, name='remove_student')
]

# <app>/ <model>_<viewtype>.html
