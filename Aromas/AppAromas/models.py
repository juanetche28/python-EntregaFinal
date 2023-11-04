from django.db import models
from django.contrib.auth.models import User


# Create your models here.

class Products(models.Model):
    title = models.CharField(max_length=20)
    description = models.CharField(max_length=40)
    code = models.CharField(max_length=7)
    price = models.IntegerField()
    status = models.CharField(max_length=20)
    stock = models.IntegerField()
    category = models.CharField(max_length=20)
    thumbnail = models.ImageField(default="productsImages/error.png", upload_to='productsImages', blank=True, null=True) 
    def __str__(self):
        return f"{self.title} - {self.code}"

class Users(models.Model):
    BASIC = "basic"
    ADMIN = "admin"
    STAFF = "staff"
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    rol_choices =[(BASIC, "Basic"), (ADMIN, "Admin"), (STAFF, "Staff")]
    age = models.IntegerField(null=True, blank=True)
    rol = models.CharField(max_length=5, choices=rol_choices, default="basic") 
    avatar = models.ImageField(default="avatares/avatar.png", upload_to='avatares')
    phone = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.user.email} - {self.rol}"

# Se guarda una vez que se compro el carrito. 
class Carts(models.Model):
    products = models.TextField(blank=True, null=True) # Diccionario de productos y qty de cada uno 
    totalCart = models.IntegerField() # Total del Carrito
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    nroInvoice = models.IntegerField(null=True, blank=True)
    dateInv = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Invoice: A-{self.nroInvoice} - Total Cart: {self.totalCart} - Buyer: {self.user}"