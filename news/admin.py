from django.contrib import admin
from news.models import News, NewsDocument, NewsImage, NewsQuote, NewsVideo


class NewsDocumentInline(admin.TabularInline):
    model = NewsDocument
    extra = 1
    fields = ('title', 'document')
    classes = ('grp-collapse grp-closed',)


class NewsImageInline(admin.TabularInline):
    model = NewsImage
    extra = 1
    fields = ('image',)
    classes = ('grp-collapse grp-closed',)


class NewsQuoteInline(admin.TabularInline):
    model = NewsQuote
    extra = 1
    fields = ('image', 'text', 'author', 'profession')
    classes = ('grp-collapse grp-closed',)


class NewsVideoInline(admin.TabularInline):
    model = NewsVideo
    extra = 1
    fields = ('video_link', 'channel_link')
    classes = ('grp-collapse grp-closed',)


@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'body1', 'body2', 'body3', 'is_active', 'is_main', 'in_main_menu', 'created_date', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('image_tag_mini', 'title', 'created_date', 'is_active', 'is_main', 'in_main_menu')
    list_editable = ('is_active', 'is_main', 'in_main_menu')
    list_filter = ('is_active', 'is_main', 'in_main_menu')
    search_fields = ('title', 'body1', 'body2', 'body3',)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )

    inlines = (NewsQuoteInline, NewsVideoInline, NewsImageInline, NewsDocumentInline)