from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('<int:product_id>/', views.detail, name='detail'),
    path('comment/create/<int:product_id>/', views.comment_create, name='comment_create'),
    path('comment/update/<int:comment_id>/', views.comment_update, name='comment_update'),
    path('comment/delete/<int:comment_id>/', views.comment_delete, name='comment_delete'),
]