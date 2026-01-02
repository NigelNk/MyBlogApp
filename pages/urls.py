from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from pages.views import HomePageView, DashboardView, EditUserProfileView

urlpatterns = [
    path('', HomePageView.as_view(), name='home'),
    path('dashboard/', DashboardView.as_view(), name='user_dashboard'),
    path('profile/<int:pk>/edit/', EditUserProfileView.as_view(), name='edit_profile'),
]


