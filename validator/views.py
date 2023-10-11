from django.shortcuts import render

# Create your views here.
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from validator.serializers import validate_id
from validator.services.id.get_birth_data import get_birth_date
from validator.services.id.get_gender import get_gender
from validator.services.id.get_governorate import get_governorate
from django.http import JsonResponse

# Create your views here.
@api_view(['POST'])
def validate(request):
    data = request.data
    try:
        validate_id(data)
        id = data.get("id")
        gender = get_gender(id)
        birth_date = get_birth_date(id)
        governorate = get_governorate(id)
    except Exception as e:
        return JsonResponse({"error": str(e.message)}, status=400)
    
    return Response({'gender': gender,
                        'birth_date': birth_date,
                        'governorate': governorate}, status=200)
