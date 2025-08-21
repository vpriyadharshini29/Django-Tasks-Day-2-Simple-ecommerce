from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import Product

# Product List
def product_list(request):
    products = Product.objects.all()
    return render(request, 'ecommerce/product_list.html', {'products': products})

# Product Detail
def product_detail(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'ecommerce/product_detail.html', {'product': product})

# Add to Cart (using session)
def add_to_cart(request, pk):
    product = get_object_or_404(Product, pk=pk)
    cart = request.session.get('cart', {})

    if str(pk) in cart:
        cart[str(pk)]['quantity'] += 1
    else:
        cart[str(pk)] = {'name': product.name, 'price': float(product.price), 'quantity': 1}

    request.session['cart'] = cart
    return redirect('cart')

# View Cart
def cart_view(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return render(request, 'ecommerce/cart.html', {'cart': cart, 'total': total})

# Remove from Cart
def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    if str(pk) in cart:
        del cart[str(pk)]
    request.session['cart'] = cart
    return redirect('cart')

# Checkout
def checkout(request):
    cart = request.session.get('cart', {})
    if not cart:
        return HttpResponse("Your cart is empty!")

    total = sum(item['price'] * item['quantity'] for item in cart.values())
    
    # Clear cart after checkout
    request.session['cart'] = {}
    return render(request, 'ecommerce/checkout.html', {'total': total})
