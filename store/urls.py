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
    product_api,
)


urlpatterns = [

    # =========================
    # HOME
    # =========================

    path(
        "",
        home,
        name="home"
    ),


    # =========================
    # PRODUCT
    # =========================

    path(
        "product/<int:id>/",
        product_detail,
        name="product_detail"
    ),


    # =========================
    # CATEGORY
    # =========================

    path(
        "category/<int:id>/",
        category_products,
        name="category_products"
    ),


    # =========================
    # CART
    # =========================

    path(
        "cart/",
        cart,
        name="cart"
    ),

    path(
        "cart/add/<int:id>/",
        add_to_cart,
        name="add_to_cart"
    ),

    path(
        "cart/remove/<int:id>/",
        remove_from_cart,
        name="remove_from_cart"
    ),

    path(
        "cart/increase/<int:id>/",
        increase_quantity,
        name="increase_quantity"
    ),

    path(
        "cart/decrease/<int:id>/",
        decrease_quantity,
        name="decrease_quantity"
    ),


    # =========================
    # AUTHENTICATION
    # =========================

    path(
        "register/",
        register,
        name="register"
    ),

    path(
        "login/",
        user_login,
        name="login"
    ),

    path(
        "logout/",
        user_logout,
        name="logout"
    ),


    # =========================
    # CHECKOUT
    # =========================

    path(
        "checkout/",
        checkout,
        name="checkout"
    ),


    # =========================
    # ORDER SUCCESS
    # =========================

    path(
        "order-success/<int:id>/",
        order_success,
        name="order_success"
    ),


    # =========================
    # ORDER HISTORY
    # =========================

    path(
        "orders/",
        order_history,
        name="order_history"
    ),


    # =========================
    # REST API
    # =========================

    path(
        "api/products/",
        product_api,
        name="product_api"
    ),
]