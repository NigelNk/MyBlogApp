from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import Article


class CreateArticle(LoginRequiredMixin, CreateView):
    model = Article
    fields = ['title', 'content', 'image']
    template_name = 'articles/create_article.html'
    login_url = reverse_lazy('login')