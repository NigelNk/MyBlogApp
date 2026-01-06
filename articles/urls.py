from django.urls import path

from .views import CreateArticle, ArticleView, ArticleDetail, PersonalArticleView

urlpatterns = [
    path('create_article/', CreateArticle.as_view(), name='create_article'),
    path('articles/', ArticleView.as_view(), name='articles'),
    path('my_articles/', PersonalArticleView.as_view(), name='personal_articles'),
    path('article-detail/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]