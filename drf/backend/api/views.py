from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from api.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializer

from rest_framework import generics, mixins
from api.authentication import TokenAuthentication

# Permissions / Authentication
from .mixins import StaffEditorPermissionsMixin

# Generic API views

class ProductDetailedApiView(StaffEditorPermissionsMixin,  # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                             generics.RetrieveAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductListApiView(StaffEditorPermissionsMixin, # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                         generics.ListAPIView):  
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    

class ProductCreateAPiView(StaffEditorPermissionsMixin,  # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                           generics.CreateAPIView):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductListCreateAPiView(StaffEditorPermissionsMixin,  # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                               generics.ListCreateAPIView):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

    def perform_create(self, serializer):
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content=content)

class ProductUpdateAPiview(StaffEditorPermissionsMixin,  # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                           generics.UpdateAPIView):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title

class ProductDestroyAPiview(StaffEditorPermissionsMixin,  # <- this permission class should always define first when inheriting, since python MRO used to find the permisson class
                            generics.DestroyAPIView):
        
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"


        
product_detail_view = ProductDetailedApiView.as_view()
product_list_create_view = ProductListCreateAPiView.as_view()
product_create_view = ProductCreateAPiView.as_view()
product_list_view = ProductListApiView.as_view()
product_update_view = ProductUpdateAPiview.as_view()
product_destroy_view = ProductDestroyAPiview.as_view()


#************************************************************************
# Mixin API views


class ProductMixins(generics.GenericAPIView, 
                    mixins.ListModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.CreateModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin):
    
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = "pk"
    
    def get(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        else:
            self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
    
    def patch(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)
    
product_mixin_view = ProductMixins.as_view()


#***************************************************************************
# Manual Made Views

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

@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):
    if request.method == 'GET':
        queryset = Product.objects.all()
        if pk is not None:
            data = queryset.filter(pk=pk).first()
            if data is None:
                return Response({"detail": "Not found"}, status=404)

            serializer = ProductSerializer(data)
            return Response(serializer.data)
        else:
            serializer = ProductSerializer(queryset, many=True)
            return Response(serializer.data)
    elif request.method == 'POST':
        queryset = Product.objects.all()
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
                serializer.save(content=content)
            return Response(f"data is validated : data = {Product.objects.last().content}")
        
    




