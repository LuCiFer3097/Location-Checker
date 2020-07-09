from django.shortcuts import render
from .models import *
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
# Create your views here.
# For Hyderabad
polygon = {"north": [17.596313, 78.266588], "east": [17.402144, 78.652482], "south": [
    17.223825, 78.446482], "west": [17.407058, 78.253541]}


class CheckBanned(generics.ListAPIView):

    def post(self, request):
        lat = request.data.get("latitude", "")
        lon = request.data.get("longitude", "")
        if lat <= polygon['north'][0] and lon < polygon['east'][1] and lat > polygon['south'][0] and lon > polygon['west'][1]:
            check = True

            return Response({"Type": "Success",
                             "Message": "Sorry this location is banned. You cannot play a paid game here."},
                            status=status.HTTP_200_OK)
        else:
            return Response({"Type": "Success",
                             "Message": "You are outside the banned circle. You can proceed and play."},
                            status=status.HTTP_200_OK)
