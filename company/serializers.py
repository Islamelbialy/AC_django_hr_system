from rest_framework import serializers 
from .models import Branches,Departments

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branches
        fields = '__all__'
