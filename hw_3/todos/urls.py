from django.contrib import admin
from django.urls import path

from .views import get_index_page, get_product_details
urlpatterns = [
    path('', get_index_page),
    path('<int:pk>', get_product_details)
]