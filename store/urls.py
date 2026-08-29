from django.urls import path
from . import views


urlpatterns = [

    path(
        '',
        views.home,
        name='home'
    ),

    path(
        'shop/',
        views.shop,
        name='shop'
    ),

    path(
        'product/<int:pk>/',
        views.product_detail,
        name='product_detail'
    ),

    path(
        'about/',
        views.about,
        name='about'
    ),

    path(
        'contact/',
        views.contact,
        name='contact'
    ),

    path(
        'cart/',
        views.cart,
        name='cart'
    ),

    path(
        'cart/add/<int:pk>/',
        views.add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/update/<int:pk>/',
        views.update_cart,
        name='update_cart'
    ),

    path(
        'cart/remove/<int:pk>/',
        views.remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'checkout/',
        views.checkout,
        name='checkout'
    ),
]