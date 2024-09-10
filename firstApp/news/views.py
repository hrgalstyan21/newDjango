from xxlimited_35 import error

from django.shortcuts import render, redirect
from .models import Article
from .forms import ArticleForm

def news(request):
    news = Article.objects.order_by('-date')[:3]
    return render(request, 'news/news_page.html', {'news':news} )

def create(request):
    error = ''
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = "Filled by wrong way"

    form = ArticleForm()

    data = {'form':form,
            'error':error
            }

    return render(request, 'news/news_create.html', data )