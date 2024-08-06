from django.urls import path
from .views import UserCreate, UserList, Home

urlpatterns = [
    path('', Home.as_view()),
    path('register/', UserCreate.as_view(), name='user-register'),
    path('users/', UserList.as_view(), name='user-list'),
]