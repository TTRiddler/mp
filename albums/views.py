from django.shortcuts import render, get_object_or_404
from django.views import View
from albums.models import Album
from pages.models import Page
from core.pagination import pagination


class AlbumsView(View):
    def get(self, request):
        albums = Album.objects.filter(is_active=True)
        albums_page = Page.objects.filter(is_active=True, action='albums').first()

        page_number = request.GET.get('page', 1)
        is_paginated, page, next_url, prev_url = pagination(albums, page_number, 10)

        context = {
            'albums': albums,
            'albums_page': albums_page,

            'is_paginated': is_paginated,
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'albums/albums.html', context)


class AlbumView(View):
    def get(self, request, album_slug):
        album = get_object_or_404(Album, slug=album_slug)
        albums_page = Page.objects.filter(is_active=True, action='albums').first()
        
        context = {
            'album': album,
            'albums_page': albums_page,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'albums/album.html', context)