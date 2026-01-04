from django.urls import path

from .views import CreateArticle

urlpatterns = [
    path('create_article/', CreateArticle.as_view(), name='create_article'),
]