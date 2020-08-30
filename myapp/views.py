# -*- coding: UTF-8 -*-
import json
import sys


import importlib

from rest_framework.generics import ListAPIView

importlib.reload(sys)
# sys.setdefaultencoding('utf8')
import json

import hashlib
from datetime import time, date
from tokenize import group

from django.core import signing
from django.http import JsonResponse

# -*- coding: utf-8 -*-
from rest_framework.response import Response

from rest_framework.views import APIView

from myapp.models import xyz,xyz1
# Create your views here.
import json
from rest_framework import serializers, generics



class Shopc(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        model = xyz  
        fields = "__all__"
        depth = 1

  

def djangojson():
    shopcart_list =  xyz.objects.all()
    serializer=Shopc(shopcart_list, many=True)#序列化
    return serializer.data  # 把数据传出去


def paper(request):
    ttt = {}
    jjj = djangojson()  # 取上面函数传出来的数据,是字典
    print(jjj)
    print("#" * 20)
    print(json.dumps(jjj))
    kkk = json.dumps(jjj).encode('utf-8').decode('unicode_escape')  # 把数据字典转为JSON对象格式,前端才可以用
    ttt["kkk"] = kkk
    return JsonResponse(kkk, safe=False, json_dumps_params={'ensure_ascii':False})


class sss(serializers.ModelSerializer):  # 并说明序列化所有字段
    class Meta:
        model = xyz1  
        fields = "__all__"
        depth = 1

  

def dddd():
    shopcart_list =  xyz1.objects.all()
    serializer=sss(shopcart_list, many=True)#序列化
    return serializer.data  # 把数据传出去


def image(request):
    ttt = {}
    jjj = dddd()  # 取上面函数传出来的数据,是字典
    print(jjj)
    print("#" * 20)
    print(json.dumps(jjj))
    kkk = json.dumps(jjj).encode('utf-8').decode('unicode_escape')  # 把数据字典转为JSON对象格式,前端才可以用
    ttt["kkk"] = kkk
    return JsonResponse(kkk, safe=False, json_dumps_params={'ensure_ascii':False})

  





