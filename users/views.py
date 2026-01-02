from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import UserAccountCreationForm
from .models import UserAccount


class UserSignupView(CreateView):
    form_class = UserAccountCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
