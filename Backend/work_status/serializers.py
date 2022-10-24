from rest_framework import serializers
from .models import *

class CoordinatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinator
        fields = ('name', 'roll_number', 'email','departments','current_task','cg','progress')

class CGSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CG
        fields = ('name','departments')

class TaskSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Task
        fields = ('name','departments')

class ProgressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Progress
        fields = ('name','departments')
