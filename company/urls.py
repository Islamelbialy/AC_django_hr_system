from django.urls import path
from .views import BrancheDetailsView,BranchesView,newBrancheView,newDepartmentToBranche

urlpatterns = [
    path('',BranchesView,name='Branches'),
    path('<int:branche_id>/',BrancheDetailsView,name='BrancheDetails'),
    path('newBranche/',newBrancheView,name='newBranche'),
    path('newDepartmentToBranche/<int:branche_id>/',newDepartmentToBranche,name='newDepartmentToBranche'),
]