from django.urls import path

from .views import CreateArticle, ArticleDetail, PersonalArticleView, ArticleDeleteView, ArticleEditView, \
    PersonalizedArticleView

urlpatterns = [
    path('create_article/', CreateArticle.as_view(), name='create_article'),
    path('my_articles/', PersonalArticleView.as_view(), name='personal_articles'),
    path('article-detail/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article_delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('edit_Article/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
    path('articles/personalized_articles/<str:username>/', PersonalizedArticleView.as_view(), name='personalized_articles'),
]