from django.urls import path
from .views import book_list

urlpatterns = [
    path("", book_list, name="book-list"),
]

from django.urls import path
from .views import user_login, user_logout, user_register

urlpatterns = [
    path("login/", user_login, name="login"),
    path("logout/", user_logout, name="logout"),
    path("register/", user_register, name="register"),
]
