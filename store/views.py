from django.shortcuts import render, get_object_or_404, redirect
from .models import Perfume


def home(request):
    featured_perfumes = Perfume.objects.filter(
        is_featured=True
    )[:4]

    return render(
        request,
        'home.html',
        {
            'featured_perfumes': featured_perfumes
        }
    )


def shop(request):
    perfumes = Perfume.objects.all()

    return render(
        request,
        'shop.html',
        {
            'perfumes': perfumes
        }
    )


def product_detail(request, pk):
    perfume = get_object_or_404(
        Perfume,
        pk=pk
    )

    return render(
        request,
        'product_detail.html',
        {
            'perfume': perfume
        }
    )


def about(request):
    return render(request, 'about.html')


def contact(request):
    return render(request, 'contact.html')


# =========================
# ADD TO CART
# =========================

def add_to_cart(request, pk):

    perfume = get_object_or_404(
        Perfume,
        pk=pk
    )

    cart = request.session.get('cart', {})

    product_id = str(perfume.id)

    quantity = int(
        request.POST.get('quantity', 1)
    )

    if product_id in cart:
        cart[product_id] += quantity
    else:
        cart[product_id] = quantity

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# CART
# =========================

def cart(request):

    cart = request.session.get(
        'cart',
        {}
    )

    cart_items = []
    cart_total = 0
    cart_count = 0

    for product_id, quantity in cart.items():

        try:
            perfume = Perfume.objects.get(
                id=product_id
            )
        except Perfume.DoesNotExist:
            continue

        total = perfume.price * quantity

        cart_items.append({
            'product': perfume,
            'quantity': quantity,
            'total': total,
        })

        cart_total += total
        cart_count += quantity

    return render(
        request,
        'cart.html',
        {
            'cart_items': cart_items,
            'cart_total': cart_total,
            'cart_count': cart_count,
        }
    )


# =========================
# UPDATE CART
# =========================

def update_cart(request, pk):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(pk)

    if product_id in cart:

        quantity = int(
            request.POST.get(
                'quantity',
                1
            )
        )

        if quantity > 0:
            cart[product_id] = quantity
        else:
            del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# REMOVE FROM CART
# =========================

def remove_from_cart(request, pk):

    cart = request.session.get(
        'cart',
        {}
    )

    product_id = str(pk)

    if product_id in cart:
        del cart[product_id]

    request.session['cart'] = cart

    return redirect('cart')


# =========================
# CHECKOUT
# =========================

def checkout(request):

    cart = request.session.get(
        'cart',
        {}
    )

    cart_items = []
    cart_total = 0

    for product_id, quantity in cart.items():

        try:
            perfume = Perfume.objects.get(
                id=product_id
            )
        except Perfume.DoesNotExist:
            continue

        total = perfume.price * quantity

        cart_items.append({
            'product': perfume,
            'quantity': quantity,
            'total': total,
        })

        cart_total += total

    return render(
        request,
        'checkout.html',
        {
            'cart_items': cart_items,
            'cart_total': cart_total,
        }
    )