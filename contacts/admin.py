from django.contrib import admin
from contacts.models import Address, Phone, Email, MapCode, Schedule, Social


@admin.register(Schedule)
class ScheduleAdmin(admin.ModelAdmin):
    list_display = ('days_point', 'time_point')


@admin.register(Social)
class SocialAdmin(admin.ModelAdmin):
    list_display = ('name', 'short_name', 'link')

admin.site.register(Address)
admin.site.register(Phone)
admin.site.register(Email)

@admin.register(MapCode)
class MapCodeAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )