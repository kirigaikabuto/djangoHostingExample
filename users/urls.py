from django.urls import path
from .views import *

urlpatterns = [
    path("login/", login_page, name="login_page"),
    path("login_action/", login_action, name="login_action"),
    path("profile/", profile_page, name="profile_page"),
]
