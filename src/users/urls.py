from django.contrib.auth.views import LoginView, LogoutView
from django.urls import path

from users.views import UserRegisterView, UserUpdateView, IndexView

app_name = 'users'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', UserRegisterView.as_view(), name='user-register'),
    path('perfil/', UserUpdateView.as_view(), name='user-profile'),
]
