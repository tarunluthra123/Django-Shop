from django.urls import path

from api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('product/create/', views.ProductCreateView.as_view(), name='product_create'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('orders/', views.OrdersView.as_view(), name='orders')
]
