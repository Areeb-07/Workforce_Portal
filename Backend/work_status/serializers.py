from rest_framework import serializers
from .models import Coordinator,CG

class CoordinatorSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Coordinator
        fields = ('name', 'roll_number', 'email','departments','current_task','cg','progress')

class CGSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = CG
        fields = ('name','departments')
