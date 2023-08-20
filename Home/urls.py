from django.urls import path
from . import views

urlpatterns = [
    path('', views.home ,name="Home" ),
    # add to card by id
    path('add_to_cart/<int:id>', views.add_to_cart, name="add_to_cart"),
    path('delete_from_cart/<int:id>', views.delete_from_cart, name="delete_from_cart"),
    path('checkout', views.checkout, name="checkout"),

    path('template', views.template, name="template"),



]