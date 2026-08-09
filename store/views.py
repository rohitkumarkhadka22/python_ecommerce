from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

from .models import Product, Order, Category
from .forms import RegisterForm


# Home
def home(request):
    products = Product.objects.all()
    categories = Category.objects.all()

    return render(
        request,
        'store/home.html',
        {
            'products': products,
            'categories': categories,
        }
    )


# Category Products
def category_products(request, category_id):
    category = get_object_or_404(Category, id=category_id)

    products = Product.objects.filter(
        category=category
    )

    return render(
        request,
        'store/category_products.html',
        {
            'category': category,
            'products': products,
        }
    )


# Product Detail
def product_detail(request, id):
    product = get_object_or_404(Product, id=id)

    return render(
        request,
        'store/product_detail.html',
        {'product': product}
    )

# Add to Cart
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)

    cart = request.session.get('cart', {})
    product_id = str(product.id)

    if product_id in cart:

        if cart[product_id] < product.stock:
            cart[product_id] += 1

    else:
        cart[product_id] = 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Cart
def cart(request):
    cart_data = request.session.get('cart', {})

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    return render(
        request,
        'store/cart.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )


# Remove from Cart
def remove_from_cart(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Increase Quantity
def increase_quantity(request, id):
    product = get_object_or_404(
        Product,
        id=id
    )

    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:

        if cart[product_id] < product.stock:
            cart[product_id] += 1

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Decrease Quantity
def decrease_quantity(request, id):
    cart = request.session.get('cart', {})
    product_id = str(id)

    if product_id in cart:

        if cart[product_id] > 1:
            cart[product_id] -= 1

        else:
            del cart[product_id]

    request.session['cart'] = cart
    request.session.modified = True

    return redirect('cart')


# Register
def register(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        form = RegisterForm(request.POST)

        if form.is_valid():

            user = form.save(commit=False)

            user.set_password(
                form.cleaned_data['password']
            )

            user.save()

            login(request, user)

            return redirect('home')

    else:
        form = RegisterForm()

    return render(
        request,
        'store/register.html',
        {'form': form}
    )


# Login
def user_login(request):

    if request.user.is_authenticated:
        return redirect('home')

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:

            login(request, user)

            return redirect('home')

        else:

            return render(
                request,
                'store/login.html',
                {
                    'error': 'Invalid username or password.'
                }
            )

    return render(
        request,
        'store/login.html'
    )


# Logout
def user_logout(request):

    logout(request)

    return redirect('home')


# Checkout
@login_required
def checkout(request):

    cart_data = request.session.get('cart', {})

    # Don't allow checkout with empty cart
    if not cart_data:
        return redirect('cart')

    cart_items = []
    total = 0

    for product_id, quantity in cart_data.items():

        product = get_object_or_404(
            Product,
            id=product_id
        )

        subtotal = product.price * quantity
        total += subtotal

        cart_items.append({
            'product': product,
            'quantity': quantity,
            'subtotal': subtotal,
        })

    # When user submits checkout form
    if request.method == 'POST':

        full_name = request.POST.get('full_name')
        phone = request.POST.get('phone')
        address = request.POST.get('address')

        order = Order.objects.create(
            user=request.user,
            full_name=full_name,
            phone=phone,
            address=address,
            total_price=total,
        )

        # Clear cart after placing order
        request.session['cart'] = {}
        request.session.modified = True

        return redirect(
            'order_success',
            id=order.id
        )

    return render(
        request,
        'store/checkout.html',
        {
            'cart_items': cart_items,
            'total': total,
        }
    )


# Order Success
@login_required
def order_success(request, id):

    order = get_object_or_404(
        Order,
        id=id,
        user=request.user
    )

    return render(
        request,
        'store/order_success.html',
        {
            'order': order
        }
    )
@login_required
def order_history(request):

    orders = Order.objects.filter(
        user=request.user
    ).order_by('-created_at')

    return render(
        request,
        'store/order_history.html',
        {
            'orders': orders
        }
    )