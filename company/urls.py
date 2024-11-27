from django.urls import path
from .views import *

urlpatterns = [
    path('',BranchesView.as_view(),name='Branches'),
    path('<int:branche_id>/',BrancheDetailsView.as_view(),name='BrancheDetails'),
    path('newBranche/',newBrancheView,name='newBranche'),
    path('newDepartmentToBranche/<int:branche_id>/',newDepartmentToBranche.as_view(),name='newDepartmentToBranche'),
    path('<int:branche_id>/<int:departmnet_id>',DepartmentDetailsView.as_view(),name='DepartmentDetails'),
    path('<int:branche_id>/<int:departmnet_id>/EditDepartment',EditDepartmentToBranche,name='EditDepartmentToBranche'),
]