from django.urls import path

from .views import CreateArticle, ArticleDetail, PersonalArticleView, ArticleDeleteView, ArticleEditView

urlpatterns = [
    path('create_article/', CreateArticle.as_view(), name='create_article'),
    path('my_articles/', PersonalArticleView.as_view(), name='personal_articles'),
    path('article-detail/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('article_delete/<int:pk>/', ArticleDeleteView.as_view(), name='article_delete'),
    path('edit_Article/<int:pk>/', ArticleEditView.as_view(), name='article_edit'),
]