from django.urls import path
from pages import views


urlpatterns = [
    path('<page_slug>/', views.PageView.as_view(), name='page'),
]