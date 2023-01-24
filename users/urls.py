from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name="register"),
    path('login/', views.login_user, name="login"),
    path('', views.login_user, name="user"),
    path('logout/', views.logout_user, name="logout"),
    path('profile/', views.profile, name="profile"),
    path('profile/<_id>', views.admin_profile, name="admin_profile"),
    path('settings/', views.settings, name="settings"),
]
