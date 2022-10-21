from django.urls import path
from . import views


app_name = 'reviews'

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create, name='create'),
    path('<int:pk>/', views.detail, name='detail'),
    path('<int:pk>/update/', views.update, name='update'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('<int:pk>/create_comment/', views.create_comment, name='create_comment'),
    path('<int:review_pk>/delete_comment/<int:comment_pk>', views.delete_comment, name='delete_comment')
]
