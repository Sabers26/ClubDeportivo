from django.urls import path
from .views import *

urlpatterns = [
    path('', inicio, name='inicio'),
    path('login', login_view, name='login'),
    path('register', register, name='register'),
    path('adminModificar', adminModificar, name='adminModificar'),
    path('forNoticias', forNoticias, name='forNoticias'),
]
