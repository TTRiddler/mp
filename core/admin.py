from django.contrib import admin
from django.contrib.flatpages.admin import FlatPageAdmin
from django.contrib.flatpages.models import FlatPage
from core.models import MainTitle, Goal, Pros, ShortAbout, ExternalLink, MailToString, MailFromString


admin.site.unregister(FlatPage)
@admin.register(FlatPage)
class PageAdmin(FlatPageAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


@admin.register(Pros)
class ProsAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


@admin.register(ShortAbout)
class ShortAboutAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )


admin.site.register(MainTitle)
admin.site.register(ExternalLink)
admin.site.register(MailToString)
admin.site.register(MailFromString)






