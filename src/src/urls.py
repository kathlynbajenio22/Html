from django.urls import path
from . import views  # Correct way to import views

urlpatterns = [
    path('', views.home, name="home"),
    path('user_registration/', views.user_registration, name="user_registration"),
    path('login/', views.login_view, name="login"),  # Renamed to avoid conflict with built-in 'login'
    path('logout/', views.logout_view, name="logout"),
    path('trainer_registration/', views.trainer_registration, name="trainer_registration"),
    path('learn_as_trainer/', views.learn_as_trainer, name="learn_as_trainer"),
]
