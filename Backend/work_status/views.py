from typing import OrderedDict

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Coordinator,CG
from .serializers import CoordinatorSerializer,CGSerializer
from rest_framework.decorators import api_view

import requests
from django.views.decorators.csrf import csrf_exempt
import base64
import datetime

class CGViewSet(viewsets.ModelViewSet):
    queryset = CG.objects.all()
    serializer_class = CGSerializer

class CoordinatorViewSet(viewsets.ModelViewSet):
    queryset = Coordinator.objects.all()
    serializer_class = CoordinatorSerializer

@api_view(['GET', 'POST'])
def coordinator_list(request):
    if request.method == 'GET':
        coordinators = Coordinator.objects.all()
        coordinator_serializer = CoordinatorSerializer(coordinators, many=True)
        return JsonResponse(coordinator_serializer.data, safe=False)
 
    elif request.method == 'POST':
        coordinator_data = JSONParser().parse(request)
        coordinator_serializer = CoordinatorSerializer(data=coordinator_data)
        if coordinator_serializer.is_valid():
            coordinator_serializer.save()
            c_id = coordinator_serializer.data['counsellor_id']
            s_id = coordinator_serializer.data['student_id']
            date = coordinator_serializer.data['date']
            start = coordinator_serializer.data['start_time']
            end = coordinator_serializer.data['end_time']
            return JsonResponse(coordinator_serializer.data, status=status.HTTP_201_CREATED) 
        return JsonResponse(coordinator_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# @api_view(['GET'])
# def upcoming(request):
#     if request.method == 'GET':
#         date,time,sid=upcoming_events()
#         l=[]
#         for i in range(len(date)):
#             a=OrderedDict([('id',i),('date',date[i]),('start_time',time[i]),('student_id',sid[i])])
#             l.append(a)
#         return JsonResponse(l, safe=False)
