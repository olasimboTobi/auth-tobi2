from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from . import views


urlpatterns = [
    path("", views.indexView, name="home"),
    path("dashboard/", views.dashboardView, name="dashboard"),
    path("register/", views.registerView, name="register"),
    path("login/", LoginView.as_view(), name="login_url"),
    path("logout", LogoutView.as_view(), name="logout"),
]