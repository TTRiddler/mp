from django.contrib import admin
from news.models import News


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'text', 'is_active', 'is_main', 'created_date', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('image_tag_mini', 'title', 'created_date', 'is_active', 'is_main')
    list_editable = ('is_active', 'is_main')
    list_filter = ('is_active', 'is_main')
    search_fields = ('title', 'text')

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )
