from django.contrib import admin
from core.models import MainTitle, Goal, Pros, ExternalLink, MailToString, MailFromString, Legacy


admin.site.register(MainTitle)
admin.site.register(ExternalLink)
admin.site.register(MailToString)
admin.site.register(MailFromString)
admin.site.register(Pros)
admin.site.register(Goal)

@admin.register(Legacy)
class LegacyAdmin(admin.ModelAdmin):
    class Media:
        js = (
            '/static/grappelli/tinymce/jscripts/tiny_mce/tiny_mce.js',
            '/static/grappelli/tinymce_setup/tinymce_setup.js',
        )






