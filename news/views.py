from django.shortcuts import render, get_object_or_404
from django.views import View
from django.http import JsonResponse
from django.template import loader
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from news.models import News
from pages.models import Page
from core.pagination import pagination


class NewsView(View):
    def get(self, request):
        news = News.objects.filter(is_active=True)
        news_page = Page.objects.filter(is_active=True, action='news').first()

        page_number = request.GET.get('page', 1)
        is_paginated, page, next_url, prev_url = pagination(news, page_number, 10)

        context = {
            'news': news,
            'news_page': news_page,

            'is_paginated': is_paginated,
            'page_object': page,
            'next_url': next_url,
            'prev_url': prev_url,
        }

        return render(request, 'news/news.html', context)


class NewsDetailView(View):
    def get(self, request, news_slug):
        news_item = get_object_or_404(News, slug=news_slug)
        news_page = Page.objects.filter(is_active=True, action='news').first()
        
        context = {
            'news_item': news_item,
            'news_page': news_page,
        }

        return render(request, 'news/news_detail.html', context)


class MoreNewsView(View):
    def post(self, request):
        page = request.POST.get('page', 2)
        news = News.objects.filter(is_active=True, is_main=False)
        
        results_per_page = 4
        paginator = Paginator(news, results_per_page)
        
        news = paginator.page(page)
        
        news_html = loader.render_to_string(
            'news/__more_news.html',
            {'news': news}
        )

        context = {
            'news_html': news_html,
            'has_next': news.has_next()
        }

        return JsonResponse(context)