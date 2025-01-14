from django.urls import path
from . import views

urlpatterns = [
 path('company/', views.company),

 # 추가
 path('', views.main, name='main'),
 path('login/', views.login, name='login'),
 path('about/', views.about, name='about'),
 path('category1/', views.category1, name='category1'),
 path('notice/',views.notice, name='notice' )
]