from django.urls import path
from . import views

app_name = 'store'

urlpatterns = [
    path('', views.allCategory, name='allCategory'),
    path('<slug:c_slug>/', views.allCategory, name='products_category'),
    path('<slug:c_slug>/<slug:p_slug>/', views.productDetail, name='productDetails'),
]
