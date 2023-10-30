from django.shortcuts import render, redirect
from AppAromas.models import  Products, Carts
from carts.carts import Cart
from AppAromas import views
from AppAromas.context_processors import totalCart
from django.contrib.auth.decorators import login_required
import json

# Create your views here.

def add_product_cart(request, pk):
    cart = Cart(request)
    product = Products.objects.get(id=pk)
    cart.addProduct(product)
    # Total del Carrito
    message = f"+1 '{product.title}' Added to cart"
    return cart_View(request, message)

def delete_product_cart(request, pk):
    cart = Cart(request)
    product = Products.objects.get(id=pk)
    cart.deleteProductCart(product)
    message = f"'{product.title}' deleted from cart"
    return cart_View(request, message)

def decrease_product_cart(request, pk):
    cart = Cart(request)
    product = Products.objects.get(id=pk)
    cart.decreaseProduct(product)
    message = f"-1 '{product.title}' decreased from cart"
    return cart_View(request, message)

def empty_cart(request):
    cart = Cart(request)
    cart.emptyCart()
    message = "Successfully Cart empty"
    return views.home(request, message)

def cart_View(request, message=None):
    if message:
        pass
    else:
        message =""
    return render(request, "AppAromas/cartView.html", {"message":message})

@login_required(login_url='/login')
def cart_Buy(request):
    cart = json.dumps(request.session["cart"])
    tCart = totalCart(request)
    strCart = str(cart)
    userID = request.user.id
    newCart = Carts (products=strCart,totalCart=tCart,user_id=userID)
    newCart.save()
    cartEmpty = Cart(request)
    cartEmpty.emptyCart()
    message="Cart buyed successfully."
    return views.home(request, message)

@login_required(login_url='/login')
def purchases_History(request):
    userID = request.user.id
    carts = Carts.objects.filter(user_id=userID)
    return render(request, "AppAromas/purchases_history.html", {"carts":carts})

@login_required(login_url='/login')
def cart_Detail(request, cartID):
    cart = Carts.objects.get(id=cartID)
    products = json.loads(cart.products)
    productsList = products.values()
    for products in productsList:
        print(f"productsList: {products}")
        print("-------------------")
    return render(request, "AppAromas/cart_detail.html", {"cart": cart, "products":productsList})