from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse, HttpResponse
import json
from api.models import Product

from rest_framework.response import Response
from rest_framework.decorators import api_view

from .serializers import ProductSerializers

@api_view(["GET"])
def api(request, *args, **kwargs):
    instance = Product.objects.all().order_by("?").first()
    print(type(instance))
    data = {}
    if instance:
        data = ProductSerializers(instance).data
    return Response(data)


