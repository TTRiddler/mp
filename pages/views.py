from django.shortcuts import render, get_object_or_404
from django.views import View
from pages.models import Page


class PageView(View):
    def get(self, request, page_slug):
        page_item = get_object_or_404(Page, slug=page_slug)
        
        context = {
            'page_item': page_item,
        }

        return render(request, 'pages/page.html', context)