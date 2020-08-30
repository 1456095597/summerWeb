from django.urls import path 
from myapp.views import *

urlpatterns =[
    path('test/', paper),
    path('test1/', image),
]