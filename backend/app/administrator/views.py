from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework import mixins

from common.authentication import JWTAuthentication

from common.serializers import UserSerializer
from core.models import User,Product,Link,Order 
from .serializers import OrderSerializer, ProductSerializers,LinkSerializer

from django.core.cache import cache
import time

class AmbassadorAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,_):
        ambassadors = User.objects.filter(is_ambassador=True)
        serializer = UserSerializer(ambassadors,many=True)
        return Response(serializer.data)
    
    
    
class ProductGenericAPIView(generics.GenericAPIView,mixins.RetrieveModelMixin,mixins.ListModelMixin,mixins.CreateModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    
    def get(self,request,pk=None):
        if pk:
            return self.retrieve(request,pk)

        return self.list(request)

    def post(self,request):
        response = self.create(request)
        
        for key in cache.keys('*'):
            if 'products_frontend' in key:
                cache.delete(key)
                
        cache.delete('products_backend')
        return response
    
    def put(self,request,pk=None):
        response = self.partial_update(request,pk)
        for key in cache.keys('*'):
            if 'products_frontend' in key:
                cache.delete(key)
        cache.delete('products_backend')
        return response
    
    def delete(self,request,pk=None):
        response = self.destroy(request,pk)
        for key in cache.keys('*'):
            if 'products_frontend' in key:
                cache.delete(key)
        cache.delete('products_backend')
        return response
    
    
class LinkAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request,user_id=None):
        links = Link.objects.filter(pk=user_id)
        serializer = LinkSerializer(links,many=True)
        return Response(serializer.data)
    
    
class OrderAPIView(APIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    
    def get(self,request):
        orders = Order.objects.filter(complete=True)
        serializer = OrderSerializer(orders,many=True)
        return Response(serializer.data)