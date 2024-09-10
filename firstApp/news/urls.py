
from django.urls import path
from . import views
from . import forms
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.news, name='news_home1'),
    path('create/', views.create, name='create_news'),
]
