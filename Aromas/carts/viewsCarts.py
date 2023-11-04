from django.shortcuts import render
from AppAromas.models import  Products, Carts
from carts.carts import Cart
from AppAromas import views
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from AppAromas.context_processors import totalCart
from django.contrib.auth.decorators import login_required
import datetime as dt  # Guardo la fecha de compra de carrito.
import json

# Create your views here.

def add_product_cartHome(request, pk):
    cart = Cart(request)
    product = Products.objects.get(id=pk)
    cart.addProduct(product)
    # Total del Carrito
    message = f"+1 '{product.title}' Added to cart"
    return views.home(request, message)

def add_product_cartView(request, pk):
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

class cartsListView(ListView):
    model = Carts
    template_name = "AppAromas/carts_list.html"

class CartsDeleteView(LoginRequiredMixin, DeleteView):
    model = Carts
    success_url = reverse_lazy("cartsListView")
    template_name = 'AppAromas/cartConfirmDelete.html'



@login_required(login_url='/login')
def cart_Buy(request):
    cart = json.dumps(request.session["cart"])
    tCart = totalCart(request)
    strCart = str(cart)
    userID = request.user.id
    nroInv = nro_invoice()
    current_date = dt.date.today()
    newCart = Carts (products=strCart,totalCart=tCart,user_id=userID, nroInvoice = nroInv, dateInv=current_date)
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
    return render(request, "AppAromas/cart_detail.html", {"cart": cart, "products":productsList})

# Funcion para generar mi numero de Factura
def nro_invoice():
    carts = Carts.objects.all()
    lenght = len(carts)
    if lenght == 0:
         nroInv = 1
    else: 
        invoices = []
        for cart in carts:
            invoices.append(cart.nroInvoice)
        nroMax = max(invoices)
        nroInv = nroMax + 1
    return (nroInv)



# --------------Vista de Clase para generar Invoice --------------

def generateInvoice(request, cartID):
    cart = Carts.objects.get(id=cartID)
    products = json.loads(cart.products)
    productsList = products.values()
    tax = (cart.totalCart * 0.21)
    total = (cart.totalCart * 1.21)    
    return render(request, "AppAromas/invoices.html", {"cart": cart, "products":productsList, "tax": tax, "total": total})

