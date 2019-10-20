from django.urls import path
from core import views


urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('change_view/', views.ChangeView.as_view(), name='change_view'),
    path('legacy/', views.LegacyView.as_view(), name='legacy'),
    path('search/', views.SearchView.as_view(), name='search'),
]