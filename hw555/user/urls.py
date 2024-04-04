from django.urls import path
from .views import login_page, register_page, handle_logout


urlpatterns = [
    path('login/', login_page, name='login_page'),
    path('register/', register_page, name='register_page'),
    path('logout/', handle_logout, name='logout'),
]