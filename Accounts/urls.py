from django.contrib import admin
from django.urls import path
from Accounts import views 

urlpatterns = [
    path('register/',views.register_user, name="register_user"),
    path('login/',views.login_user, name="login_user"),
    path('logout/',views.logout_user, name="logout_user"),
]

