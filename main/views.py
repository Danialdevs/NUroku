from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import HttpResponseNotFound
from .models import Class, News

#  Получение групп обучения текущего пользователя
# Create your views here.
def home(request):
  return render(request, 'modl/login.html')

def news(request):
  news = News.objects.all()
  return render(request, 'feed/news.html', {'news': news})
  
def user_detail(request, pk):
    user = User.objects.get(pk=pk)
    return render(request, 'feed/user.html', {'user': user})

def new(request, id):
    new = News.objects.get(id=id)
    return render(request, 'feed/new.html', {'new': new})



def teacher_view(request):
    if request.user.is_authenticated and hasattr(request.user, 'teacher'):
        # user is authenticated and is a teacher
        return render(request, 'teacher_template.html')
    else:
        # user is not authenticated or is not a teacher
        return redirect('login')