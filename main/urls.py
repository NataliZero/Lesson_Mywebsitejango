from django.urls import path
from . import views  # Импортируем views из текущего приложения

urlpatterns = [
    path('', views.index, name='home'),  # Главная страница
    path('page1/', views.page1, name='page1'),  # Страница 1
    path('page2/', views.page2, name='page2'),  # Страница 2
    path('page3/', views.page3, name='page3'),  # Страница 3
]
