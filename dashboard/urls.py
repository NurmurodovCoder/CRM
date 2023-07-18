from django.urls import path
from .views import index, login_user, register_user, logout_user


urlpatterns = [
    path('', index, name='index'),
    path('login_user/', login_user, name='login_user'),
    path('register_user/', register_user, name='register_user'),
    path('logout/', logout_user, name='logout_user')
]
