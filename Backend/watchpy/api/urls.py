# myapp/urls.py
from django.urls import path
from .views import RegisterUser, LoginUser, UserList, UserDetail, api_root

urlpatterns = [
    path('', api_root),
    path('register/', RegisterUser.as_view(), name='register'),
    path('login/', LoginUser.as_view(), name='login'),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>/', UserDetail.as_view(), name='user-detail'),
]
