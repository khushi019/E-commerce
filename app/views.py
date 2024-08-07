from django.shortcuts import render,redirect
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth import login, logout, authenticate
import os

# Create your views here.

def homeView(request):
    print(os.environ.get("a"))
    return render(request,'app/home.html')

def storeView(request):
    products = Product.objects.all()
    return render(request, 'app/store.html', {'products': products})

def product_category_view(request, subcategory):
    products = Product.objects.filter(product__product_category=subcategory)
    context = {
        'subcategory': subcategory,
        'products': products
    }
    return render(request, 'app/product.html', context)


def add_to_cart(request, product_id):
    if not request.user.is_authenticated:
        return redirect('login')
    
    product = Product.objects.get(id=product_id)
    cart_item, created = Cart.objects.get_or_create(user=request.user, product=product)
    if not created:
        cart_item.quantity += 1
        cart_item.save()
    
    # Redirect back to the provided current URL
    current_url = request.POST.get('current_url', 'add_to_cart')
    return redirect(current_url)

@login_required
def cart_view(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity

    context = {
        'cart_items': cart_items,
        'total_price': total_price
    }
    return render(request, 'app/cart.html', context)
@login_required
def remove_from_cart(request, cart_item_id):
    cart_item = Cart.objects.get(id=cart_item_id, user=request.user)
    cart_item.delete()
    return redirect('cart_view')


@login_required
def update_quantity(request, item_id, action):
    # Get the cart item or return a 404 if not found
    cart_item = Cart.objects.get( id=item_id, user=request.user)
    
    # Determine the action and update the quantity accordingly
    if action == 'increase':
        cart_item.quantity += 1
    elif action == 'decrease':
        # Ensure quantity does not drop below 1
        if cart_item.quantity > 1:
            cart_item.quantity -= 1
        else:
            # Remove the item from the cart if quantity is 1 and decrease action is taken
            cart_item.delete()
    else:
        # If the action is not recognized, redirect to the cart view
        return redirect('cart_view')

    # Save the updated cart item and redirect to the cart view
    cart_item.save()
    return redirect('cart_view')

@login_required
def checkout(request):
    cart_items = Cart.objects.filter(user=request.user)
    total_price = sum(item.product.price * item.quantity for item in cart_items)
    for item in cart_items:
        item.total_price = item.product.price * item.quantity
    
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            order = form.save(commit=False)
            order.user = request.user
            order.total_price = total_price
            order.save()
            
            # Create OrderItems
            for cart_item in cart_items:
                OrderItem.objects.create(
                    order=order,
                    product=cart_item.product,
                    quantity=cart_item.quantity,
                    price=cart_item.product.price
                )
            
            # Clear the cart
            cart_items.delete()
            
            return redirect('order_confirmation', order_id=order.id)
    else:
        form = OrderForm()

    context = {
        'form': form,
        'cart_items': cart_items,
        'total_price': total_price,
    }
    
    return render(request, 'app/checkout.html', context)

@login_required
def order_confirmation(request, order_id):
    order = Order.objects.get(id=order_id, user=request.user)
    return render(request, 'app/order_confirmation.html', {'order': order})

@login_required
def my_orders(request):
    orders = Order.objects.filter(user=request.user)
    return render(request, 'app/my_orders.html', {'orders': orders})

@login_required
def order_detail(request, order_id):
    order = Order.objects.get( id=order_id, user=request.user)
    return render(request, 'app/order_detail.html', {'order': order})

def signupView(request):
    if request.method=='POST':
        form=UserCreationForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=UserCreationForm()    
    return render(request,'app/signup.html',{'form':form})