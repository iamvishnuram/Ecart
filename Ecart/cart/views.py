from django.shortcuts import render,redirect,get_object_or_404
from store.models import Product
from . models import Cart,CartItem
from django.core.exceptions import ObjectDoesNotExist

def cart_id(request):
    cart = request.session.session_key
    if not cart:
        cart = request.session.create()
    return cart
    
def addcart(request, product_id):
    product = Product.objects.get(id=product_id)
    try:
        cart = Cart.objects.get(cartid=cart_id(request))
    except ObjectDoesNotExist:
        cart = Cart.objects.create(
            cartid = cart_id(request)
        )
        cart.save()
    
    try:
        cart_item = CartItem.objects.get(product=product, cart=cart)
        if cart_item.quantity < cart_item.product.stock:
            cart_item.quantity +=1
        cart_item.save()
    except CartItem.DoesNotExist:
        cart_item = CartItem.objects.create(
            product=product,
            quantity=1,
            cart=cart
        )
        cart_item.save()
    return redirect('cart:cart_detail')

def cart_detail(requset, total=0, counter=0, cart_items=None):
    try:
        cart = Cart.objects.get(cartid=cart_id(requset))
        cart_items = CartItem.objects.filter(cart=cart, active=True)
        for cart_item in cart_items:
            total += (cart_item.product.price * cart_item.quantity)
            counter += cart_item.quantity
    except ObjectDoesNotExist:
        pass
    return render(requset, 'cart.html', dict(cart_items=cart_items, total=total, counter=counter))

def remove(request, id):
    cart = Cart.objects.get(cartid=cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    if cart_item.quantity > 1:
        cart_item.quantity -=1
        cart_item.save()
    else:
        cart_item.delete()
        
    return redirect('cart:cart_detail')

def delete(request, id):
    cart = Cart.objects.get(cartid=cart_id(request))
    product = get_object_or_404(Product, id=id)
    cart_item = CartItem.objects.get(product=product, cart=cart)
    cart_item.delete()
    return redirect('cart:cart_detail')
    
def checkout(request):
    return render(request, 'checkout.html')

