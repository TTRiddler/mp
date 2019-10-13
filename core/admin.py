from django.contrib import admin
from django.contrib.flatpages.admin import FlatpageForm, FlatPageAdmin
from django import forms
from django.contrib.flatpages.models import FlatPage
from tinymce.widgets import TinyMCE
from core.models import *


@admin.register(TitleTag)
class TitleTagAdmin(admin.ModelAdmin):
    list_display = ('url', 'seo_title', 'seo_desc', 'seo_kwrds')
    fields = ('url', 'seo_title', 'seo_desc', 'seo_kwrds')


class FlatPageForm(forms.ModelForm):
    content = forms.CharField(widget=TinyMCE())

    class Meta:
        model = FlatPage
        fields = '__all__'


admin.site.unregister(FlatPage)

@admin.register(FlatPage)
class PageAdmin(FlatPageAdmin):
    form = FlatPageForm


admin.site.register(MainTitle)
admin.site.register(Goal)
admin.site.register(Pros)
admin.site.register(ShortAbout)
admin.site.register(ExternalLink)
admin.site.register(MailToString)
admin.site.register(MailFromString)







