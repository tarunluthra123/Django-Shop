from rest_framework.generics import (CreateAPIView, ListAPIView, ListCreateAPIView)
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from api import serializers, models


class HelloView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class ProductsListView(ListAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()


class ProductCreateView(CreateAPIView):
    serializer_class = serializers.ProductSerializer
    queryset = models.Product.objects.all()
    permission_classes = (IsAuthenticated,)


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
        productId = request.body['productId']
        product = models.Product.objects.filter(id=productId)
        serializer = self.serializer_class()

    def get_queryset(self):
        return models.Order.objects.all()


