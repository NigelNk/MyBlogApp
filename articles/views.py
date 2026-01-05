from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView

from .forms import ArticleForm
from .models import Article


class CreateArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    context_object_name = 'article'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return  super().form_valid(form)

class ArticleView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/articles.html'
    login_url = reverse_lazy('login')