from django.urls import path
from documents import views


urlpatterns = [
    path('<document_category_slug>/', views.DocumentCategoryView.as_view(), name='document_category'),
]