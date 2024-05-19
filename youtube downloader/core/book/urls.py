from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('api/movies/recommendations/', views.get_movie_recommendations, name='get_movie_recommendations'),
    path('login/', views.login_page, name='login'),
    path('register/', views.register_page, name='register'),
    path('logout/', views.custom_logout, name='logout'),
]
