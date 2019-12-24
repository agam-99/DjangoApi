from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
import bcrypt
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import User
from django.core import serializers
import json
from django.forms.models import model_to_dict
from django.core import serializers
@csrf_exempt

def register(request):
    # print(request.body)
    # req=serializers.serialize("json",request)
    # data = serializers.serialize("json", request.body)
    # print(data)
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # return JsonResponse({"status": "REGISTRATION SUCCESS","data":body.get("name")})
    errors = User.objects.validator(body)
    if len(errors):
        # for tag, error in errors.iteritems():
        #     messages.error(request, error, extra_tags=tag)
        return JsonResponse({"status": "ERROR","data":errors})

    hashed_password = bcrypt.hashpw(body['password'].encode(), bcrypt.gensalt()).decode('utf-8')
    user = User(name=body['name'], mobile=body['mobile'], password=hashed_password, email=body['email'],username=body['username'])
    # body_unicode = user.decode('utf-8')
    user.save()
    # user = json.loads(body_unicode)
    # request.session['id'] = user.id
    return JsonResponse({"status": "REGISTRATION SUCCESS"})

@csrf_exempt

def login(request):
    body_unicode = request.body.decode('utf-8')
    body = json.loads(body_unicode)
    # print(User.objects.filter(username=body['username']).exists())
    if (User.objects.filter(username=body['username']).exists()):
        user = User.objects.filter(username=body['username'])[0]
        if (bcrypt.checkpw(body['password'].encode('utf-8'), user.password.encode('utf-8'))):
            dict_obj = model_to_dict( user )
            return JsonResponse({"status": "OK","name":dict_obj["name"],"mobile":dict_obj["mobile"],"email":dict_obj["email"]})
        return JsonResponse({"status": "WRONG PASSWORD"})
    return JsonResponse({"status": "NO SUCH USERNAME"})
