from django.urls import path
from . import views

app_name='reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:reviews_pk>/', views.detail, name='detail'),
    path('reviews/<int:reviews_pk>/update/', views.update, name='update'),
    path('reviews/delete/', views.delete, name='delete'),
]
