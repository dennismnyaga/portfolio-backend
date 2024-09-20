from rest_framework.serializers import ModelSerializer, ImageField, PrimaryKeyRelatedField, ListField
from . models import *
from rest_framework import serializers



class ProjectStateSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProjectState
        fields = '__all__'


class TechStackSerializer(serializers.ModelSerializer):
    class Meta:
        model = TechStack
        fields = '__all__'

    

class PotfolioSerializer(serializers.ModelSerializer):
    stacks = TechStackSerializer(many=True, read_only = True)
    state_of_project = ProjectStateSerializer( read_only = True)

    class Meta:
        model = Porfolio
        fields = '__all__'