from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from api.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer

from rest_framework import generics

@api_view(["POST"])
def api(request, *args, **kwargs):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        data = request.data
        print(f"data is validated {data}")
        return Response(data)
    else:
        return Response(serializer.errors, status=400)
    

class ProductDetailedApiView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductCreateAPiView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

product_detail_view = ProductDetailedApiView.as_view()
product_create_view = ProductCreateAPiView.as_view()


