from django.contrib import admin
from django.urls import path
from AppAromas import views
from carts import viewsCarts
from django.conf import settings
from django.contrib.auth import views as auth_views
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
    path('productsConfirmReset/', views.productsConfirmReset, name="products_Confirm_Reset"),
    
]

# ---- URLS de Carts ----
urlpatterns += [
    path('cartBuy/', viewsCarts.cart_Buy, name="cartBuy"),
    path('purchasesHistory/', viewsCarts.purchases_History, name="purchasesHistory"),
    path('cartDetail/<int:cartID>/', viewsCarts.cart_Detail, name="cartDetail"),
    path('cartsListView/', viewsCarts.cartsListView.as_view(), name="cartsListView"),
    path('CartsDeleteView/<int:pk>/', viewsCarts.CartsDeleteView.as_view(), name="CartsDeleteView"),
    path('cartView/', viewsCarts.cart_View, name="cartView"),
    path('deletePk/<int:pk>/', viewsCarts.delete_product_cart, name="deleteProductCart"),
    path('decreasePk/<int:pk>/', viewsCarts.decrease_product_cart, name="decreaseProductCart"),
    path('addProduct/<int:pk>/', viewsCarts.add_product_cartHome, name="addToCartHome"),
    path('addPk/<int:pk>/', viewsCarts.add_product_cartView, name="addToCartView"),
]


# ---- URLS de Invoice PDF ----
urlpatterns += [
    path('invoices/<int:cartID>', viewsCarts.generateInvoice, name="generateInvoice"),
]


urlpatterns += [
    path('reset/password_reset', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('reset/password_reset_done', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
]


#Para las imagenes
urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
urlpatterns+= static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)