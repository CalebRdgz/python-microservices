from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Product, User
from .serializers import ProductSerializer
import random


# Create your views here.
class ProductViewSet(viewsets.ViewSet):
    def list(self, request): #list of the products one by one /api/products route, GET request
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True) #list of products, returns an array
        return Response(serializer.data)

    def create(self, request): #/api/products, POST request
        serializer = ProductSerializer(data=request.data)
        serializer.is_valid(raise_exception=True) #ask if the serializer is valid
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None): #/api/products/<str: id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    def update(self, request, pk=None): #/api/products/<str: id>
        product = Product.objects.get(id=pk)
        serializer = ProductSerializer(instance=product, data=request.data) #product that we have, data we want to update
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None): #/api/products/<str: id>
        product = Product.objects.get(id=pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
    def get(self, _): #wont use request parameter, so use _
        users = User.objects.all()
        #get a random user:
        user = random.choice(users)
        return Response({
            "id": user.id
        })