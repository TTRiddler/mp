from django.urls import path
from feedback import views
from core.decorators import check_recaptcha


urlpatterns = [
    path('add/', check_recaptcha(views.FeedBackView.as_view()), name='feedback'),
]