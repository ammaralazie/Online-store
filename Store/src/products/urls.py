from django.urls import path
from . import views

app_name='product'
urlpatterns = [
    path('', views.products_list, name='products_list'),
    path('cart/', views.cart, name='cart'),
    path('checkout/', views.checkout, name='checkout'),
    path('<slug:slug>',views.product_detail,name='product_detail'),
    path('update_item/',views.updateItem,name='updateItem'),
    path('addAndRemovItem/',views.addAndRemovItem,name='addAndRemovItem'),
    path('processOrder/',views.processOrder,name='processOrder'),

]
