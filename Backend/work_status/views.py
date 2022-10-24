from typing import OrderedDict

from django.shortcuts import render
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import *
from .serializers import *
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

class TaskViewSet(viewsets.ModelViewSet):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class ProgressViewSet(viewsets.ModelViewSet):
    queryset = Progress.objects.all()
    serializer_class = ProgressSerializer

@api_view(['POST','PUT'])
def coordinator(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        data_list=[]
        coordi_detail = Coordinator.objects.filter(roll_number=data['roll_number'])
        if len(coordi_detail)==0:
            coordi = Coordinator(roll_number=data['roll_number'],name=data['name'],email=data['email'],departments=data['departments'])
            coordi.save()
            return JsonResponse(data_list,safe=False)
        else:
            coordi = coordi_detail[0]
            if coordi.name is None:
                coordi.name = data['name']
                coordi.departments=data['departments']
                coordi.email=data['email']
                coordi.save()
        for task in Progress.objects.filter(task_number__startswith=data['roll_number']):
            task_details = Task.objects.filter(task_id=task.task_id)[0]
            cg_details = CG.objects.filter(email=task_details.cg_email)[0]
            progress_data = OrderedDict([('task_id',task.task_number),('task',task_details.task),('sub_task',task_details.sub_task),('cg',cg_details.name+', '+cg_details.department),('progress',task.progress)])
            data_list.append(progress_data)
        return JsonResponse(data_list,safe=False)
    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        task = Progress.objects.filter(task_number=data['task_id'])[0]
        if task.progress=='Assigned':
            task.progress='In Progress'
        elif task.progress=='In Progress':
            task.progress='Completed'
        task.save()
        return JsonResponse({"success":"true"},safe=False)

@api_view(['POST','PUT'])
def cg(request):
    if request.method == 'POST':
        coordi_list=[]
        data = JSONParser().parse(request)
        for task_detail in Task.objects.filter(cg_email=data['email']):
            for task in Progress.objects.filter(task_id=task_detail.task_id):
                coordi = Coordinator.objects.filter(roll_number=task.task_number[:-4])[0]
                coordi_data = OrderedDict([('name',coordi.name),('roll_number',coordi.roll_number),('task',task_detail.task),('sub_task',task_detail.sub_task),('progress',task.progress)])
                coordi_list.append(coordi_data)
        task_dict=OrderedDict()
        for task_name in Task.objects.filter(cg_email=data['email']).order_by().values_list('task').distinct():
            sub_task_list=[]
            for task_detail in Task.objects.filter(task=task_name[0]):
                task = OrderedDict([('task_id',task_detail.task_id),('sub_task',task_detail.sub_task)])
                sub_task_list.append(task)
            task_dict[task_name[0]]=sub_task_list
        cg_data = OrderedDict([('coordi_list',coordi_list),('task_list',task_dict)])
        return JsonResponse(cg_data,safe=False)

    elif request.method == 'PUT':
        data = JSONParser().parse(request)
        if len(Coordinator.objects.filter(roll_number=data['roll_number']))==0:
            coordi = Coordinator(roll_number=data['roll_number'],name='',email='',departments='')
            coordi.save()
        task_number=data['roll_number']
        coordi_tasks = Progress.objects.filter(task_number__startswith=data['roll_number'])
        if len(coordi_tasks)!=0:
            for i in range(4-len(str(len(coordi_tasks)+1))):
                task_number+='0'
            task_number+=str(len(coordi_tasks)+1)
        else:
            task_number+='0001'
        task = Progress(task_number=task_number,task_id=data['task_id'],progress='Assigned')
        task.save()
        return JsonResponse({"success":"true"},safe=False)