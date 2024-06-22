




from django.shortcuts import get_object_or_404, redirect, render


from store.models import Product
from .models import Cart, CartItem


def cart_detail(request):
    cart1, created = Cart.objects.get_or_create(user =request.user)
    cart = CartItem.objects.filter(cart=cart1)
    return render(request, 'cart/cart_detail.html', {'cart': cart, 'cart1':cart1})
    
def add_to_cart(request, id):
    product = get_object_or_404(Product, id=id)
    cart, created = Cart.objects.get_or_create(user=request.user)
    cart_item, created = CartItem.objects.get_or_create(cart=cart, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    return redirect('cart:cart_detail')

def update_cart(request, id):
    cart1 = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=id)
    cart = get_object_or_404(CartItem, cart=cart1, product=product)
    if request.method == 'POST':
        quantity = request.POST.get('quantity')
        if quantity:
            cart.quantity = int(quantity)
            cart.save()
    return redirect('cart:cart_detail')


def remove_from_cart(request, id):
    cart = get_object_or_404(Cart, user=request.user)
    product = get_object_or_404(Product, id=id)
    cart_item = get_object_or_404(CartItem, cart=cart, product=product)
    cart_item.delete()
    return redirect('cart:cart_detail')