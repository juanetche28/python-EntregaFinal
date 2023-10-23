from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class ProductForm(forms.Form):
    #Especifico los campos
    title = forms.CharField(max_length=20)
    description = forms.CharField(max_length=40)
    code = forms.CharField(max_length=7)
    price = forms.IntegerField()
    status = forms.CharField(max_length=20)
    stock = forms.IntegerField()
    category = forms.CharField(max_length=20)
    thumbnail = forms.ImageField()

class UserForm(forms.Form):
    firstName = forms.CharField(max_length=20)
    lastName = forms.CharField(max_length=20)
    email = forms.EmailField(max_length=20)
    age = forms.IntegerField()
    password = forms.CharField(max_length=20)
    rol = forms.CharField(max_length=20)

class CartForm(forms.Form):
    product = forms.CharField(max_length=5)
    qty = forms.IntegerField()

class BuscaProductForm(forms.Form):
    product = forms.CharField()


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        # Si queremos EDIAR los mensajes de ayuda editamos este dict,
            # de lo contrario lo limpiamos de ésta forma.
        help_text = {k: "" for k in fields}
