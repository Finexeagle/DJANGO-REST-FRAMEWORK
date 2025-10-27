from django.shortcuts import render
from django.forms.models import model_to_dict
from django.http import JsonResponse
import json
from api.models import Product

def api(request, *args, **kwargs):
    model = Product.objects.all().order_by("?").first()
    print(type(model))
    data = {}
    if model:
        data = model_to_dict(model, fields=['id', 'title'])
    return JsonResponse(data)


