from django.urls import path
from .views import inicio, login_view, register

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
]
