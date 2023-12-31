from django.contrib import admin
from django.urls import path
from AppAromas import views
#Para las imagenes
from django.conf import settings
from django.conf.urls.static import static

# ---- URLS Generales ----
urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name="home"),
    path('search/', views.search, name="search"),
]

# ---- URLS de Sesion ----
urlpatterns += [
    path('login/', views.loginUser, name="login"),
    path('register', views.registerUser, name='register'),
    path('logout', views.logoutUser, name='logout'),
]

# ---- URLS de Usuario ----
urlpatterns += [
    path('profile/', views.profile, name="profile"),
    path('editProfile/', views.editProfile, name="editProfile"),
    path('delete_User/<user_id>', views.delete_User, name="delete_User"),
    path('userConfirmDeleteView/<user_id>', views.userConfirmDeleteView, name="userConfirmDeleteView"),
    path('usersListView/', views.usersListView.as_view(), name="usersListView"),
]

# ---- URLS de Productos ----
urlpatterns += [
    path('productsForm/', views.productsForm, name="productsForm"),
    path('editProduct/<product_id>', views.editProduct, name="editProduct"),
    path('confirmDeleteProduct/<product_id>', views.confirmDeleteProduct, name="confirmDeleteProduct"),
    path('deleteProduct/<product_id>', views.deleteProduct, name="delete_Product"),
    path('resetProducts/', views.resetProducts, name="reset_Products"),
]

# ---- URLS de Carts ----
urlpatterns += [
    path('cartsForm/', views.cartsForm, name="cartsForm"),
    path('cartBuy/', views.cartBuy, name="cartBuy"),
    path('cartsListView/', views.cartsListView.as_view(), name="cartsListView"),
    path('CartsDeleteView/<int:pk>/', views.CartsDeleteView.as_view(), name="CartsDeleteView"),
]


#Para las imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)