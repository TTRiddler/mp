from django.contrib import admin
from core.models import MainTitle, Goal, Pros, ExternalLink, MailToString, MailFromString


admin.site.register(MainTitle)
admin.site.register(ExternalLink)
admin.site.register(MailToString)
admin.site.register(MailFromString)
admin.site.register(Pros)
admin.site.register(Goal)






