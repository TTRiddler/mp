from django.shortcuts import render, redirect
from django.views import View
from django.db.models import Q
from core.models import *
from pages.models import Page
from news.models import News
from documents.models import Document
from albums.models import Album


class IndexView(View):
    def get(self, request):
        index_page = Page.objects.filter(is_active=True, action='home').first()
        external_links = ExternalLink.objects.all()
        proses = Pros.objects.all()
        goals = Goal.objects.all()

        try:
            main_news = News.objects.filter(is_active=True, is_main=True).first()
        except:
            main_news = News.objects.filter(is_active=True).first()

        news = News.objects.filter(is_active=True, is_main=False)[:4]
        main_menu_news = News.objects.filter(is_active=True, in_main_menu=True)

        context = {
            'index_page': index_page,
            'external_links': external_links,
            'proses': proses,
            'goals': goals,
            'main_news': main_news,
            'news': news,
            'main_menu_news': main_menu_news,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'core/index.html', context)


class ChangeView(View):
    def get(self, request):
        is_lo = request.session.get('is_lo')

        request.session['is_lo'] = True if not is_lo else False

        return redirect('index')


class LegacyView(View):
    def get(self, request):
        legacy = Legacy.objects.first()

        context = {
            'legacy': legacy,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'core/legacy.html', context)


class SearchView(View):
    def get(self, request):
        query = request.GET.get('query')

        if query:
            pages = Page.objects.filter(is_active=True, action='pages')
            news = News.objects.filter(is_active=True)
            documents = Document.objects.all()
            albums = Album.objects.filter(is_active=True)

            pages = pages.filter(
                Q(title__icontains=query)|
                Q(body1__icontains=query)|
                Q(body2__icontains=query)|
                Q(body3__icontains=query)
            ).distinct()
            
            news = news.filter(
                Q(title__icontains=query)|
                Q(body1__icontains=query)|
                Q(body2__icontains=query)|
                Q(body3__icontains=query)
            ).distinct()

            documents = documents.filter(
                Q(name__icontains=query)|
                Q(category__title__icontains=query)
            ).distinct()

            albums = albums.filter(
                Q(title__icontains=query)|
                Q(description__icontains=query)
            ).distinct()
        else:
            pages = []
            news = []
            documents = []
            albums = []

        context = {
            'q_pages': pages,
            'q_news': news,
            'q_documents': documents,
            'q_albums': albums,
        }

        lo = 'lo/' if request.session.get('is_lo') else ''
        return render(request, lo + 'core/search.html', context)
