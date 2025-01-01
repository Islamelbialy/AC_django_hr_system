from rest_framework import viewsets
from .serializers import BranchesSerializer
from .models import Branches

class BrancheViewSet(viewsets.ModelViewSet): 
   queryset = Branches.objects.all() 
   serializer_class = BranchesSerializer