from django.contrib import admin
from news.models import News, MainNews


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'is_active', 'created_date', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('title', 'created_date', 'is_active')
    list_editable = ('is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'text')


@admin.register(MainNews)
class MainNewsAdmin(admin.ModelAdmin):
    autocomplete_fields = ('news',)

