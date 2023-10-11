from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

# Create your views here.
@api_view(['GET'])
def endpoints(request):
    data = ['/tes','/tes/:hello']
    return Response(data)