from django.urls import path
from . import views
from .views import (
  PostListView,
  PostDetailView,
  PostCreateView,
  PostUpdateView,
  PostDeleteView
  )
urlpatterns = [
    path('', PostListView.as_view(), name='home-page'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('Map/', views.about, name='home-map'),
    path('students/', views.studentManagement, name='student-management'),
    path('students/update/',views.Management_detail, name='management-detail'),
]

# <app>/ <model>_<viewtype>.html
