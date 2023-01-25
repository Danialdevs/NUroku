from django.shortcuts import render
from .models import article, category


# Create your views here.
def index(request):
    categorys = category.objects.all()
    return render(request, 'index.html', {'categorys': categorys})


def Categoryview(request, id):
    categorya = category.objects.get(id=id)
    articles = article.objects.filter(category_id=id)
    return render(request, 'cat.html', {
        'articles': articles,
        'categorya': categorya
    })


def article_detail(request, pk):
    art = article.objects.get(id=pk)
    return render(request, 'article.html', {'art': art})
