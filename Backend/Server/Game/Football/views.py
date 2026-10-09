import io
from django.shortcuts import render
from rest_framework.parsers import JSONParser
from django.http import JsonResponse
from rest_framework.views import csrf_exempt
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from .serializers import StudentSerializer,courseSerializer
from .models import Student, Course
# Create your views here.
def home(request):
    return HttpResponse('<h1>Hello world</h1>')


@csrf_exempt
def students(request):
    if request.method == "POST":
        data = request.body
        dataIO = io.BytesIO(data)
        parser_data = JSONParser().parse(dataIO)
        serializer = StudentSerializer(data=parser_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"student_created":"Successful"}, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "GET":
        data = Student.objects.all()
        serializer = StudentSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False, status=200)
    
@csrf_exempt
def singleStudent(request,id):
    if request.method == "GET":
        std = Student.objects.get(id=id)
        serializer = StudentSerializer(std)
        return JsonResponse(serializer.data)
    return JsonResponse(serializer.error,status=400)

@api_view(["POST","GET"])
def courses(request):
    if request.method == "POST":
        data = request.body
        dataIo= io.BytesIO(data)
        parser_data = JSONParser().parse(dataIo)

        serializer = courseSerializer(data=parser_data, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"created":"successful"}, status=201)
        return JsonResponse(serializer.errors, status=400)
    elif request.method == "GET":
        data = Course.objects.all()
        serializer = courseSerializer(data, many=True)
        return JsonResponse(serializer.data, safe=False)