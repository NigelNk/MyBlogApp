from django.urls import path

from .views import CreateArticle, ArticleView

urlpatterns = [
    path('create_article/', CreateArticle.as_view(), name='create_article'),
    path('articles/', ArticleView.as_view(), name='articles'),
]