from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.

class HelloApiView(APIView):
    "test API view"
    def get(self, request, format=None):
        an_view = ["Uses HTTP method as (PUT, GET POST, patch, delete)",
                   "is simmilat to traditional diango view"]
        return Response({'message':'Siema!', 'an_apiview': an_view})