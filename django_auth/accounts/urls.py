from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

# accounts는 앱네임 지정 안한대

urlpatterns = [
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="accounts/login.html"),
        name="login",
    ),  # 설정 재정의
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
    path("signup/", views.signup, name="signup"),
    path("profile/", views.profile, name="profile"),
]