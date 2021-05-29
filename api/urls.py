from django.urls import path

from api import views

urlpatterns = [
    path('hello/', views.HelloView.as_view(), name='hello'),
    path('products/', views.ProductsListView.as_view(), name='products'),
    path('orders/', views.OrdersView.as_view(), name='orders'),
    path('register/', views.CreateNewUserView.as_view(), name='register_user'),
    path('user/', views.RetrieveUpdateUserView.as_view(), name='get_update_user'),
    path('product/<int:pk>', views.RetrieveProductView.as_view(), name='get_product')
]
