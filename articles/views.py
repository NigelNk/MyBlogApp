from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DetailView, ListView, DeleteView, UpdateView

from .forms import ArticleForm
from .models import Article

from django.contrib.auth import get_user_model
User = get_user_model()


class CreateArticle(LoginRequiredMixin, CreateView):
    form_class = ArticleForm
    template_name = 'articles/create_article.html'
    context_object_name = 'article'
    login_url = reverse_lazy('login')
    success_url = reverse_lazy('personal_articles')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)


class PersonalArticleView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'articles/personal_articles.html'
    login_url = reverse_lazy('login')

    ordering = ['created_at']
    paginate_by = 3

    def get_queryset(self):
        return Article.objects.filter(author=self.request.user)


class ArticleDetail(LoginRequiredMixin, DetailView):
    model = Article
    template_name = 'articles/article_detail.html'
    context_object_name = 'article'
    login_url = reverse_lazy('login')


class ArticleDeleteView(LoginRequiredMixin, DeleteView):
    model = Article
    template_name = 'articles/article_delete.html'
    success_url = reverse_lazy('personal_articles')
    login_url = reverse_lazy('login')
    context_object_name = 'article'

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()

        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        messages.success(self.request, 'Article deleted successfully')
        return super().form_valid(form)


class ArticleEditView(LoginRequiredMixin, UpdateView):
    form_class = ArticleForm
    model = Article
    template_name = 'articles/article_edit.html'
    context_object_name = 'article'
    success_url = reverse_lazy('personal_articles')
    login_url = reverse_lazy('login')

    def dispatch(self, request, *args, **kwargs):
        obj = self.get_object()
        if obj.author != self.request.user:
            raise PermissionDenied
        return super().dispatch(request, *args, **kwargs)

    def form_valid(self, form):
        form.instance.edited = True
        messages.success(self.request, 'Article updated successfully')
        return super().form_valid(form)


class PersonalizedArticleView(ListView):
    model = Article
    template_name = "articles/personalized_article.html"
    context_object_name = 'articles'

    paginate_by = 3

    def get_queryset(self):
        self.author = get_object_or_404(User, username=self.kwargs['username'])
        return Article.objects.filter(author=self.author).select_related('author')

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["author"] = self.author
        return context
