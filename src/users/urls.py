from django.urls import path
from django.contrib.auth import views as auth_views
from .views import profile_update, profiles_get,Register

urlpatterns=[
    # path("login/",auth_views.LoginView.as_view(),name="login"),
    path("profiles_get/",profiles_get),
    path("<int:user_id>/profile_update/",profile_update),
    path("register/",Register.as_view()),
]
