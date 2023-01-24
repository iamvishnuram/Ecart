from django.urls import path
from . import views

app_name = "cart"

urlpatterns = [
    path('add/<int:product_id>/', views.addcart, name='add_cart'),
    path('', views.cart_detail, name="cart_detail"),
    path('remove/<int:id>/', views.remove, name="remove"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('checkout/', views.checkout, name='checkout'),
]
