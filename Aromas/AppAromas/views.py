from django.shortcuts import render
from AppAromas.models import  Products, Users, Carts, User
from AppAromas.forms import CartForm, BuscaProductForm, UserRegisterForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView
from django.views.generic.edit import DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
import json

# Create your views here.

# Creo una funcion que me devuelve el rol del usuario
def validateRol(request):
    if  Users.objects.filter(user_id=request.user.id).exists():
        userSearched =  Users.objects.get(user_id=request.user.id)
        rol = userSearched.rol
    else:
        rol = "user" 
    return(rol)

def home(request, message=None):
    products = Products.objects.all() #trae todos los productos
    rol =  validateRol(request)  # Funcion que me devuelve el Rol
    contexto= {"products":products}
    if message is not None:
        pass
    else:
        message = ""
    return render(request, "AppAromas/index.html",{"contexto":contexto, "rol":rol, "message":message})

def search(request):
    if request.method == "POST":
        miFormulario = BuscaProductForm(request.POST) # Aqui me llega la informacion del html
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            products = Products.objects.filter(category__icontains=informacion["product"])
            return render(request, "AppAromas/search_results.html", {"products": products})
    else:
        miFormulario = BuscaProductForm()

    return render(request, "AppAromas/search.html", {"miFormulario": miFormulario})

# -------------- Vista de Clase --------------
class usersListView(ListView):
    model = Users
    template_name = "AppAromas/users_list.html"

# -------------- Vistas de Usuarios --------------
@login_required(login_url='/login')
def delete_User(request, user_id):
    print(f"Id a eliminar: {user_id}")
    user = User.objects.get(id=user_id)
    user.delete()
    # vuelvo al menú
    message = "User Deleted"
    return home(request, message)

@login_required(login_url='/login')
def userConfirmDeleteView(request, user_id):
    print(f"Id a confirmar: {user_id}")
    user = Users.objects.get(id=user_id)
    contexto = {"user": user}
    rol =  validateRol(request)  # Funcion que me devuelve el Rol
    return render(request, "AppAromas/userConfirmDeleteView.html", {"contexto":contexto, "rol":rol})


@login_required(login_url='/login')
def profile(request):
    userID = request.user.id
    firstName = request.user.first_name
    lastName = request.user.last_name
    email = request.user.email
    username = request.user.username
    if  Users.objects.filter(user_id=userID).exists():
        userSearched =  Users.objects.get(user_id=userID)
        rol = userSearched.rol
        avatar = userSearched.avatar
        age = userSearched.age
        phone = userSearched.phone
        address = userSearched.address
    else:
        rol = "none"
        avatar = "/avatares/avatar1.png"
        age = "none"
        address = "none"
        phone = "none"
    contexto= {"firstName":firstName, "lastName":lastName,"email":email,"username":username, "rol":rol, "avatar":avatar, "age":age, "phone":phone, "address":address} 
    return render(request, "AppAromas/profile.html", {'contexto':contexto})

@login_required(login_url='/login')
def editProfile(request):
    # Mis usuarios tienen dos tablas, la propia de django (User) y otra con campos adicionales (Users)
    userRequest = request.user
    if request.method =='POST'or request.method == 'FILES':
        userRequest.last_name=request.POST['lastName']
        userRequest.first_name=request.POST['firstName']
        userRequest.email=request.POST['email']
        userRequest.save()
        if Users.objects.filter(user_id=userRequest.id).exists():
            userFinded = Users.objects.select_for_update().get(user_id=userRequest.id)
            userFinded.age = request.POST['age']
            userFinded.phone = request.POST['phone']
            userFinded.address = request.POST['address']
            filepath = request.FILES.get('avatar', False)
            if filepath == False:
                pass
            else:
                userFinded.avatar = request.FILES['avatar']
            contexto= {"firstName":userRequest.first_name, "lastName":userRequest.last_name,"email":userRequest.email,"username":userRequest.username, "rol":userFinded.rol, "avatar":userFinded.avatar, "age":userFinded.age, "phone":userFinded.phone, "address":userFinded.address} 
            userFinded.save()
            return render(request, "AppAromas/profile.html",  {'contexto':contexto})
        else:
            filepath = request.FILES.get('avatar', False)
            if filepath == False:
                avatar = "avatares/avatar1.png"
            else:
                avatar = request.FILES['avatar']
            newUser = Users (age=request.POST['age'], phone=request.POST['phone'], address=request.POST['address'], avatar = avatar, user_id = userRequest.id)          
            contexto= {"firstName":userRequest.first_name, "lastName":userRequest.last_name,"email":userRequest.email,"username":userRequest.username, "rol":newUser.rol, "avatar":newUser.avatar, "age":newUser.age, "phone":newUser.phone, "address":newUser.address} 
            newUser.save()
            return render(request, "AppAromas/profile.html",  {'contexto':contexto})
    else:
        userID = request.user.id
        firstName = request.user.first_name
        lastName = request.user.last_name
        email = request.user.email
        username = request.user.username
        if  Users.objects.filter(user_id=userID).exists():
            userSearched =  Users.objects.get(user_id=userID)
            rol = userSearched.rol
            avatar = userSearched.avatar
            age = userSearched.age
        else:
            rol = "none"
            avatar = "/avatares/avatar.png"
            age = "none"
        contexto= {"firstName":firstName, "lastName":lastName,"email":email,"username":username, "rol":rol, "avatar":avatar, "age":age} 
        return render(request, "AppAromas/editProfile.html", {'contexto':contexto})


# -------------- Vistas de Sesiones (Login, Register y Logout) --------------
def loginUser(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data = request.POST)
        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            contrasena = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=contrasena)
            if user is not None:
                login(request, user)
                message="Successfully logged user."
                return home(request, message)
            else:
                return render(request, "AppAromas/login.html", {"message":"Data error. Please try again.", 'form':form})
        else:
            return render(request, "AppAromas/login.html", {"message": "Error, Wrong Form", 'form':form})
    form = AuthenticationForm()
    return render(request, "AppAromas/login.html", {'form':form})

def registerUser(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            form.save()
            message="Successfully registered user."
            return home(request, message)
    else:  
        form = UserRegisterForm()     
    return render(request,"AppAromas/register.html" ,  {"form":form})

@login_required(login_url='/login')
def logoutUser(request):
    logout(request)
    message="User correctly logged out."
    return home(request, message)


# --------------Vista de Productos --------------
@login_required(login_url='/login')
def productsForm(request):
    if request.method =='POST'or request.method == 'FILES':
        filepath = request.FILES.get('thumbnail', False)
        if filepath == False:
            thumbnail = "productsImages/error.png"
        else:
            thumbnail = request.FILES['thumbnail']
        product = Products (title=request.POST['title'],description=request.POST['description'],code=request.POST['code'],price=request.POST['price'],status=request.POST['status'],stock=request.POST['stock'],category=request.POST['category'],thumbnail=thumbnail)
        product.save()
        message="Product added successfully"
        return home(request, message)
    else:
        return render(request, "AppAromas/productsForm.html")

@login_required(login_url='/login')                    
def editProduct(request, product_id):
    product = Products.objects.select_for_update().get(id=product_id)
    if request.method =='POST' or request.method == 'FILES':
        product.title = request.POST['title']
        product.description = request.POST['description']
        product.code = request.POST['code']
        product.price = request.POST['price']
        product.status = request.POST['status']
        product.stock = request.POST['stock']
        product.category = request.POST['category']
        filepath = request.FILES.get('thumbnail', False)
        if filepath == False:
            pass
        else:
            product.thumbnail = request.FILES['thumbnail']
        product.save()
        message="Product edited successfully"
        return home(request, message)
    else:
        return render(request, "AppAromas/editProduct.html", {"product":product})

def resetProducts(request):
    products = Products.objects.all()  # trae todos los productos
    products.delete() #Borro todos los productos
    #Ahora voy a importar mi base de productos desde el arhcivo JSON
    with open("AppAromas/static/AppAromas/importJSON/productsBase.json") as contenido:
        informacion = json.load(contenido) #trae todos los productos del .JSON
        for p in informacion:  #Recorro todo mi diccionario y agrego cada producto a la base de datos
            product = Products (title=p['title'],description=p['description'],code=p['code'],price=p['price'],status=p['status'],stock=p['stock'],category=p['category'], thumbnail=p['thumbnail'])
            product.save()
            message="You have reset the product database successfully." 
    return home(request, message)

@login_required(login_url='/login')
def confirmDeleteProduct(request, product_id):
    products = Products.objects.get(id=product_id)
    contexto = {"products": products}
    rol =  validateRol(request)  # Funcion que me devuelve el Rol
    return render(request, "AppAromas/confirmDeleteProduct.html", {"contexto":contexto, "rol":rol})

@login_required(login_url='/login')
def deleteProduct(request, product_id):
    product = Products.objects.get(id=product_id)
    product.delete()
    # vuelvo al menú
    message="Product deleted successfully"
    return home(request, message)


# --------------Vista de Carts --------------
def cartsForm(request):
    if request.method =='POST':
        miFormulario = CartForm(request.POST)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            cart = Carts(product=informacion['product'],qty=informacion['qty'])
            cart.save()
            message="Cart added successfully."
            return home(request, message)
    else:
        miFormulario = CartForm()
    return render(request, "AppAromas/cartsForm.html", {"miFormulario": miFormulario})

class cartsListView(ListView):
    model = Carts
    template_name = "AppAromas/carts_list.html"

class CartsDeleteView(LoginRequiredMixin, DeleteView):
    model = Carts
    success_url = reverse_lazy("cartsListView")
    template_name = 'AppAromas/confirmDeleteCart.html'

def cartBuy(request):
    message="Product buyed successfully."
    return home(request, message)
