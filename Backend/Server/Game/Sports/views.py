from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.parsers import JSONParser
import io
from django.views.decorators.csrf import csrf_exempt
from .models import Club, Team
from .serializers import ClubSerializer, TeamSerializer
# Create your views here.
#--------------------------------All about CLUB VIEWS-----------------------------------------
# create a POST and GET all information about Club
@csrf_exempt
def  Clubs(request):
    if request.method == "POST":
        club_quest = request.body
        club_io = io.BytesIO(club_quest)
        club_parser = JSONParser().parse(club_io)

        serializer = ClubSerializer(data=club_parser, many=True)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Club created":"Successful"}, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "GET":
        club_data = Club.objects.all()
        serializer = ClubSerializer(club_data, many=True)
        return JsonResponse(serializer.data,safe=False, status=200)
    
#create a GET for one Single Club
@csrf_exempt
def singleClub(request,id):
    if request.method == "GET":
        data = Club.objects.get(club_id=id)
        serializer = ClubSerializer(data)
        return JsonResponse(serializer.data)


@csrf_exempt
def singleClubs(request, query):
    if request.method == "GET":
        try:
            # 1. Check if the user searched using an ID
            if query.isdigit():
                data = Club.objects.get(club_id=query)
            
            # 2. Otherwise, look up by name (case-insensitive)
            else:
                data = Club.objects.get(name__iexact=query)
                
            serializer = ClubSerializer(data)
            return JsonResponse(serializer.data, status=200)
            
        except Club.DoesNotExist:
            return JsonResponse({"error": "Club not found"}, status=404)
#--------------------------------End of CLUB VIEWS-----------------------------------------


#-------------------------  CREATE POST AND GET ALL TEAMS ---------------------------
@csrf_exempt
def teamAll ( request):
    if request.method == "POST":
        team_data = request.body
        team_io = io.BytesIO(team_data)
        team_parse = JSONParser().parse(team_io)
        serializer = TeamSerializer(data=team_parse, many=True)

        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"Team created":"successful"}, status=201)
        return JsonResponse(serializer.errors, status=400)

    if request.method == "GET":
        get_data = Team.objects.all()
        serializer = TeamSerializer(get_data, many=True)
        return JsonResponse(serializer.data, safe=False)

#--------------------end Team View-----------------------------------------------------------