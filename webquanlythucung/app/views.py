import os
import solcx
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpRequest
from .serializers import UserSerializer
from .serializers import ThuCungSerializer
from django.http import JsonResponse
from app.blockchain_web3.pet_provider import PetProvider
from rest_framework.response import Response
from .models import User
from .models import ThuCung
import json
# Create your views here.
def home(request):
    return render(request,'home.html')
@csrf_exempt   
def petshtml(request):
    my_variable = request.GET.get('myVariable', None)
    user = User.objects.get(idmetamaxk=my_variable)
    thucung = ThuCung.objects.filter(user=user)
    thucungdautien = ThuCung.objects.filter(id=1)
    context = {'items': thucung,'itemsfine':thucungdautien}
    return render(request,'app/Pets.HTML',context)

@api_view(['POST'])
def add(request):
    serializer = ThuCungSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@csrf_exempt
def connectedMetaMask(request):
    if request.method == 'POST':
        data_received = json.loads(request.body.decode('utf-8'))
        # Xử lý dữ liệu ở đây
        value = data_received.get("idmetamaxk")
        print(value)
        # Trả về phản hồi
        try:
            user = User.objects.get(idmetamaxk=value)

        except User.DoesNotExist:
            # Đối tượng không tồn tại
            serializer = UserSerializer(data=data_received)
            if serializer.is_valid():
                serializer.save()
        return JsonResponse(data_received)
    else:
        # Trả về lỗi nếu request không phải là POST
        response_data = {'status': 'error', 'message': 'Invalid request method'}
        return JsonResponse(response_data)

@api_view(['GET'])
def getFollowFather(request, pk):
    thucung = ThuCung.objects.get(id=pk)
    fatherthucung = ThuCung.objects.filter(id=thucung.father)
    return JsonResponse(fatherthucung)
@api_view(['GET'])
def getFollowMother(request, pk):
    thucung = ThuCung.objects.get(id=pk)
    motherthucung = ThuCung.objects.filter(id=thucung.mother)
    return JsonResponse(motherthucung)
@api_view(['GET'])
def check(request):
    owner = '0x1B5DA21C1dBF8F1B88b0c7eE0A70830C6bDDEe70'
    father = '0x1234567890123456789012345678901234567890'
    mother = '0x1234567890123456789012345678901234567890'
    information = "information"
    key = '0x4f473bf56b3a5454f88a94d99aebb3b0c57c131b7e436cecfd59be1790bcfe16'
    Pet = PetProvider().get_pet_MyInformation(owner,father,mother,information,key)
    return HttpRequest(Pet)
@api_view(['GET'])
def update(request):
    newowner = '0x1B5DA21C1dBF8F1B88b0c7eE0A70830C6bDDEe70'
    information = "newinformation"
    key = '0x4f473bf56b3a5454f88a94d99aebb3b0c57c131b7e436cecfd59be1790bcfe16'
    Pet = PetProvider().update_pet(information,newowner,key)
    return HttpRequest(Pet)
    