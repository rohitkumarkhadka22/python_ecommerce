from django.urls import path

from .views import (
    home,
    product_detail,
    category_products,
    add_to_cart,
    cart,
    remove_from_cart,
    increase_quantity,
    decrease_quantity,
    register,
    user_login,
    user_logout,
    checkout,
    order_success,
    order_history,
)


urlpatterns = [

    # Home
    path(
        '',
        home,
        name='home'
    ),

    # Categories
    path(
        'category/<int:category_id>/',
        category_products,
        name='category_products'
    ),

    # Product Detail
    path(
        'product/<int:id>/',
        product_detail,
        name='product_detail'
    ),

    # Cart
    path(
        'cart/add/<int:id>/',
        add_to_cart,
        name='add_to_cart'
    ),

    path(
        'cart/',
        cart,
        name='cart'
    ),

    path(
        'cart/remove/<int:id>/',
        remove_from_cart,
        name='remove_from_cart'
    ),

    path(
        'cart/increase/<int:id>/',
        increase_quantity,
        name='increase_quantity'
    ),

    path(
        'cart/decrease/<int:id>/',
        decrease_quantity,
        name='decrease_quantity'
    ),

    # Authentication
    path(
        'register/',
        register,
        name='register'
    ),

    path(
        'login/',
        user_login,
        name='login'
    ),

    path(
        'logout/',
        user_logout,
        name='logout'
    ),

    # Checkout
    path(
        'checkout/',
        checkout,
        name='checkout'
    ),

    # Order Success
    path(
        'order-success/<int:id>/',
        order_success,
        name='order_success'
    ),

    # Order History
    path(
        'orders/',
        order_history,
        name='order_history'
    ),

]

