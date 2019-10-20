from django.urls import path
from news import views


urlpatterns = [
    path('', views.NewsView.as_view(), name='news'),
    path('detail/<news_slug>/', views.NewsDetailView.as_view(), name='news_detail'),
    path('more/', views.MoreNewsView.as_view(), name='more_news'),
]