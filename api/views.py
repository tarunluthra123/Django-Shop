from django.contrib.auth.models import User
from rest_framework.generics import (ListCreateAPIView, CreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView)
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly, AllowAny
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers, models

class HelloView(APIView):
    permission_classes = [IsAuthenticated,]

    def get(self, request):
        msg = 'Hello ' + request.user.first_name + ' ' + request.user.last_name
        return Response({'msg': msg})


class ProductsListView(ListCreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (IsAuthenticatedOrReadOnly,)


class OrdersView(ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.OrderSerializer

    def list(self, request, *args, **kwargs):
        username = request.user
        orders = models.Order.objects.filter(user=username)
        serializer = self.serializer_class(orders, many=True)
        return Response(serializer.data)

    def create(self, request, *args, **kwargs):
        user = request.user
        if 'productId' not in request.data:
            return Response({"detail": "productId Field missing", "code": "missing_field"}, status=400)
        productId = request.data['productId']
        new_order = {
            "product": productId,
            "user": user.id,
            "delivered": False
        }
        serializer = self.serializer_class(data=new_order)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response({"detail": "Could not create new order", "code": "error_creating_new_order",
                             "errors": serializer.errors}, status=400)

    def get_queryset(self):
        return models.Order.objects.all()


class CreateNewUserView(CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = serializers.RegisterSerializer


class RetrieveUpdateUserView(RetrieveUpdateAPIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = serializers.RegisterSerializer

    def get(self, request, *args, **kwargs):
        user = request.user
        response = {
            "username": user.username,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "email": user.email
        }
        return Response(response, status=200)

    def get_queryset(self):
        queryset = User.objects.all()
        return queryset


class RetrieveProductView(RetrieveAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (AllowAny,)
