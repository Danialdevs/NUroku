from django.urls import path,re_path
from . import views
from django.http import HttpResponse
from django.contrib.auth import views as auth_views



urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('user/<int:pk>/',views.user_detail, name='user_detail'),
    path('news/<int:id>/',views.new, name='new'),
    path('login/', auth_views.LoginView.as_view(template_name='feed/login.html'), name='login'),

]
