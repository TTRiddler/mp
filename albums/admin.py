from django.contrib import admin
from albums.models import Album, ImageInAlbum


class ImageInAlbumInline(admin.TabularInline):
    model = ImageInAlbum
    extra = 0


@admin.register(Album)
class AlbumAdmin(admin.ModelAdmin):
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'is_active', 'created_date', 'image', 'image_tag')
        }),
        ('SEO', {
            'fields': ('slug', 'seo_title', 'seo_desc', 'seo_kwrds'),
        }),
    )

    prepopulated_fields = {'slug': ('title',)}
    readonly_fields = ('image_tag',)
    list_display = ('title', 'created_date', 'is_active')
    list_editable = ('created_date', 'is_active',)
    list_filter = ('is_active',)
    search_fields = ('title', 'description')
    inlines = (ImageInAlbumInline,)
