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
    rol = models.CharField(max_length=5, choices=rol_choices, default="user", blank=True, null=True) 
    avatar = models.ImageField(default="avatares/avatar.png", upload_to='avatares')
    phone = models.CharField(max_length=40, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    def __str__(self):
        return f"{self.user.email} - {self.rol}"


class Carts(models.Model):
    #products = models.CharField(max_length=100) # Desarrollar. Deberia ser un array que tenga el codigo de producto y qty de cada producto agregado al carrito.
    product = models.CharField(max_length=5) # Iria el codigo del producto. 
    qty = models.IntegerField() # Cantidad del producto
    user = models.ForeignKey(User, blank=True, null=True, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.product} - Quantity: {self.qty}"