from django.shortcuts import render
from django.http import JsonResponse
import json
# Create your views here.
# def api(request, *args, **kwargs):
#     print(request.body)
#     return(JsonResponse({"data":2}))

def api(request, *args, **kwargs):
    body = request.body # byte string of json data
    data = {}
    try:
        data = json.loads(body) # conveerts byte string to a json string
    except:
        pass
    print(data)
    print(request.GET) # getting the Query params 
    print(request.headers) # django object
    print(request.content_type) # django object
    print(json.dumps(dict(request.headers))) # django object
    return(JsonResponse({"data":2}))


