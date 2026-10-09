from django.shortcuts import render
from rest_framework.views import APIView
from django.contrib.auth import authenticate
from rest_framework.authtoken.models import Token
from django.contrib.auth.models import User
from rest_framework.response import Response
# Create your views here.

class loging(APIView):
    queryset = User.objects.all()
    def post(self, request):
        username = request.data.get('username')
        password = request.data.get('password')
        user = authenticate(
            username = username,
            password = password
        )
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)
            return Response({'Token':token.key})
        return Response(
            {'error': 'Invalid username or password'}, 
            status=401
        )
    def get(self, request,*args, **kwargs):
        print(request.user)
        response = super().get(request, *args, **kwargs)
        return response