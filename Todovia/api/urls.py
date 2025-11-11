from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TaskInfoViewSet, RegisterAPI, LoginAPI

# Router for viewsets
router = DefaultRouter()
router.register(r'taskInformation', TaskInfoViewSet, basename='taskInformation')

app_name = 'api'
# API endpoints
urlpatterns = [
    path('RegisterAPI/', RegisterAPI.as_view(), name='RegisterAPI'),  # User registration
    path('LoginAPI/', LoginAPI.as_view(), name='LoginAPI'),  # User login
    path('', include(router.urls)),  # TaskInfo endpoints (CRUD)
]
