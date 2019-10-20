from django.shortcuts import render
from django.views import View
from core.models import *
from pages.models import Page
from news.models import News


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

        context = {
            'index_page': index_page,
            'external_links': external_links,
            'proses': proses,
            'goals': goals,
            'main_news': main_news,
            'news': news,
        }

        return render(request, 'core/index.html', context)
