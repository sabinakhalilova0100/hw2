from django.urls import path
from .views import login_page, register_page, handle_logout

urlpatterns = [
    # products/
    path('login/', login_page, name='login-page'),
    path('register/', register_page, name='register-page'),
    path('logout/', handle_logout, name='logout')
    # path('forgot-password/'),
    # path('reset-password'),
]