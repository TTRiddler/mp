from django.urls import path
from albums import views


urlpatterns = [
    path('', views.AlbumsView.as_view(), name='albums'),
    path('<album_slug>/', views.AlbumView.as_view(), name='album'),
]