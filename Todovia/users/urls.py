from django.urls import path
from users import views


app_name = 'users'  # Enables namespaced URLs like 'users:loginUser'

# URL patterns for user authentication and management
urlpatterns = [
    path('users/createUser/', views.createUser, name='createUser'),  # Register a new user
    path('', views.loginUser, name='loginUser'),  # Log in existing user
    path('users/logoutUser/', views.logoutUser, name='logoutUser'),  # Log out current user
]
