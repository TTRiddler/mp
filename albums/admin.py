from django.contrib import admin
from albums.models import Album, ImageInAlbum


class ImageInAlbumInline(admin.TabularInline):
    model = ImageInAlbum
    extra = 0
    classes = ('grp-collapse grp-closed',)


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'is_active', 'created_date', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
            'classes': ('grp-collapse grp-closed',),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('image_tag_mini', 'title', 'created_date', 'is_active')
    list_editable = ('created_date', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    inlines = (ImageInAlbumInline,)

    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )
