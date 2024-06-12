from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Empty (root) path goes to the index view
    path('', views.index, name='home'),
    path("login/", auth_views.LoginView.as_view(), name="login"),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("about", views.about, name="about"),
]