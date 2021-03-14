from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('login/', views.login, name="login"),
    path('logout/', views.logout, name="logout"),
    path('signup/', views.register, name="signup"),
    path('Profile/', views.profile, name="profile"),
    path('Dashboard/', views.dashboard, name="dashboard"),
]