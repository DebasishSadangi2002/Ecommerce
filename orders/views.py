# orders/views.py
from django.shortcuts import get_object_or_404, render, redirect
from .models import Order, OrderItem
from .forms import OrderCreateForm
from cart.models import Cart, CartItem
# orders/views.py
from django.contrib.auth.decorators import login_required


@login_required
def order_create(request):
    try:
        cart = Cart.objects.get(user=request.user)
        
    except Cart.DoesNotExist:
        cart = None

    if cart is None or not cart.items.exists():
        return redirect('cart:cart_detail')  # Redirect to cart if empty

    if request.method == 'POST':
        form = OrderCreateForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.save()
            for item in cart.items.all():
                OrderItem.objects.create(
                    order=order,
                    product=item.product,
                    quantity=item.quantity,
                    price=item.get_total_price(),
                )
            cart.items.all().delete()  # Clear the cart
            return redirect('orders:order_created', order_id=order.id)
    else:
        form = OrderCreateForm()
    return render(request, 'orders/create.html', {'form': form, 'cart': cart})

@login_required
def order_created(request, order_id):
    order = Order.objects.get(id=order_id)
    return render(request, 'orders/created.html', {'order': order})

@login_required
def order_history(request):
    orders = Order.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'orders/history.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id, user=request.user)
    return render(request, 'orders/detail.html', {'order': order})