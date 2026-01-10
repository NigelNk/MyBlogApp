from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import TemplateView, ListView, UpdateView

from articles.models import Article
from users.models import UserProfile, UserAccount


class HomePageView(ListView):
    model = Article
    context_object_name = 'articles'
    template_name = "pages/index.html"
    ordering = ['created_at']
    paginate_by = 3


class DashboardView(LoginRequiredMixin, ListView):
    model = Article
    context_object_name = 'articles'
    template_name = 'pages/dashboard.html'
    login_url = reverse_lazy('login')

    ordering = ['-created_at']
    paginate_by = 3

    def get_queryset(self):
        queryset = super().get_queryset().order_by('-created_at')
        category = self.request.GET.get('category')

        if category and category != 'all':
            queryset = queryset.filter(category=category)

        return queryset


class EditUserProfileView(LoginRequiredMixin, UpdateView):
    model = UserProfile
    fields = ['first_name', 'last_name', 'image_url', 'short_bio', 'long_bio', 'facebook', 'twitter', 'linkedin']
    template_name = 'users/edit_profile.html'
    login_url = reverse_lazy('login')

    def get_object(self, queryset=None):
        profile, created = UserProfile.objects.get_or_create(user=self.request.user)
        return profile

    def form_valid(self, form):
        messages.success(self.request, 'Profile updated successfully')
        return super().form_valid(form)
