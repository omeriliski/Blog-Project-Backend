from django.urls import path
from django.contrib.auth import views as auth_views
from .views import get_profiles,get_update_profile,Register

urlpatterns=[
    # path("login/",auth_views.LoginView.as_view(),name="login"),
    path("get_profiles/",get_profiles),
    path("<int:user_id>/get_update_profile/",get_update_profile),
    path("register/",Register.as_view()),
]
