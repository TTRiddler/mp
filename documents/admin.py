from django.contrib import admin
from documents.models import Document, DocumentCategory


class DocumentInline(admin.TabularInline):
    model = Document
    extra = 0
    fields = ('name', 'document')


@admin.register(DocumentCategory)
class DocumentCategoryAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'is_active')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title',)
    inlines = (DocumentInline,)
