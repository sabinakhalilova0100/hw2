from django.urls import path

from .views import lists_page_view, product_details_view, delete_list_page_view, edit_list_page_view

urlpatterns = [
    path('', lists_page_view, name='lists'),
    path('<int:pk>', product_details_view, name='product_details'),
    path('lists/<int:pk>/delete/', delete_list_page_view, name='delete_list_page'),
    path('lists/<int:pk>', product_details_view, name='product_details_page'),
    path('lists/<int:pk>/edit/', edit_list_page_view, name='edit_list_page'),




]