from django.urls import path
from .views import index_page, product_details, delete_list



urlpatterns = [
    path('', index_page),
    path('<int:pk>', product_details),
    path('<int:pk>/delete/', delete_list)

]