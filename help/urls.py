from django.urls import path,re_path
from . import views
from django.http import HttpResponse


urlpatterns = [
    path('', views.index, name='index'),
    path('Category/<int:id>/',views.Categoryview, name='Categoryview'),
    path('article/<int:pk>/',views.article_detail, name='article_detail'),


]
