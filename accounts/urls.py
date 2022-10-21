from django import views
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path('', views.index, name='index'),
    path("signup/", views.signup, name="signup"),
    path("login/", views.login, name="login"),
    path("logout/", views.logout, name="logout"),
    path("update/", views.update, name="update"),
    path("pwupdate/", views.pwupdate, name="change_password"),
    path("delete/", views.delete, name="delete"),
    path("detail/", views.detail, name="detail"),
    path("user_detail/<int:pk>/", views.user_detail, name="user_detail"),
]
