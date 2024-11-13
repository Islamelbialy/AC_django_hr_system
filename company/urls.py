from django.urls import path
from .views import BrancheDetailsView,BranchesView,newBrancheView,newDepartmentToBranche,DepartmentDetailsView,EditDepartmentToBranche

urlpatterns = [
    path('',BranchesView,name='Branches'),
    path('<int:branche_id>/',BrancheDetailsView,name='BrancheDetails'),
    path('newBranche/',newBrancheView,name='newBranche'),
    path('newDepartmentToBranche/<int:branche_id>/',newDepartmentToBranche,name='newDepartmentToBranche'),
    path('<int:branche_id>/<int:departmnet_id>',DepartmentDetailsView,name='DepartmentDetails'),
    path('<int:branche_id>/<int:departmnet_id>/EditDepartment',EditDepartmentToBranche,name='EditDepartmentToBranche'),
]