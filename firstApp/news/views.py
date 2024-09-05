from django.shortcuts import render
from .models import Article

def news(request):
    news = Article.objects.order_by('-date')[:3]
    return render(request, 'news/news_page.html', {'news':news} )
