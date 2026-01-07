from django.contrib import messages
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView

from .forms import UserAccountCreationForm
from .models import UserAccount


class UserSignupView(CreateView):
    form_class = UserAccountCreationForm
    template_name = 'users/signup.html'
    success_url = reverse_lazy('login')
    
    def form_valid(self, form):
        messages.success(self.request, 'Account created successfully, please login')
        return  super().form_valid(form)
