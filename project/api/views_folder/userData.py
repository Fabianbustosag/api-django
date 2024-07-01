from rest_framework.views import APIView
from rest_framework.response import Response
from api.models import UserData
from django.http import JsonResponse
from ..models import UserData
from django.views.decorators.csrf import csrf_exempt
from ..serializers import *
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

#Obtener info
@api_view(['GET'])
def get_user_data(request,user_id):
    if request.method == 'GET':
        try:
            user_data = UserData.objects.get(user_id=user_id)
            user_data_dict = {
                'intolerance_allergies': user_data.intolerance_allergies,
                'home_size': user_data.home_size,
                'name_user': user_data.name_user,
                'age': user_data.age,
                'month_budget': user_data.month_budget,
                'user_id': user_data.user_id,
                'type_count': user_data.type_count,
                'biography': user_data.biography,
                'phone': user_data.phone
            }
            return JsonResponse(user_data_dict)
        except UserData.DoesNotExist:
            return JsonResponse({'error': 'User data not found'}, status=404)

#Create
@csrf_exempt
@api_view(['POST'])
def post_new_user(request):
    if request.method == 'POST':
        serializer = UserDataSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("User created", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Update
@api_view(['PUT'])
def update_user_data(request, user_id):
    try:
        user_data = UserData.objects.get(user_id=user_id)
    except UserData.DoesNotExist:
        return JsonResponse({'error': 'User data not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = UserDataSerializer(user_data, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#Delete
@api_view(['DELETE'])
def delete_user_data(request, user_id):
    try:
        user_data = UserData.objects.get(user_id=user_id)
    except UserData.DoesNotExist:
        return JsonResponse({'error': 'User data not found'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        user_data.delete()
        return JsonResponse({'message': 'User data deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
