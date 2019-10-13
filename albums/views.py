from django.shortcuts import render, get_object_or_404
from django.views import View
from albums.models import Album


class AlbumsView(View):
    def get(self, request):
        albums = Album.objects.filter(is_active=True)

        context = {
            'albums': albums,
        }

        return render(request, 'albums/albums.html', context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)
        
        context = {
            'album': album,
        }

        return render(request, 'albums/album.html', context)