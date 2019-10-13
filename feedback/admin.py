from django.contrib import admin
from feedback.models import FeedBack


@admin.register(FeedBack)
class FeedBackAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'created_date')