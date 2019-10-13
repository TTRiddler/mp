from django.shortcuts import render, get_object_or_404
from django.views import View
from documents.models import Document, DocumentCategory


class DocumentCategoryView(View):
    def get(self, request, document_category_slug):
        document_category = get_object_or_404(DocumentCategory, slug=document_category_slug, is_active=True)
        document_categories = DocumentCategory.objects.filter(is_active=True)

        context = {
            'document_category': document_category,
            'document_categories': document_categories,
        }

        return render(request, 'documents/document_category.html', context)
