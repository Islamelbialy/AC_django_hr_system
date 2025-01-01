from django.urls import path,include
from .views import *
from .APIs import *
from rest_framework import routers

router = routers.DefaultRouter() 
router.register(r'getBranches', BrancheViewSet)


urlpatterns = [
    path('',BranchesView.as_view(),name='Branches'),
    path('<int:branche_id>/',BrancheDetailsView.as_view(),name='BrancheDetails'),
    path('newBranche/',newBrancheView,name='newBranche'),
    path('newDepartmentToBranche/<int:branche_id>/',newDepartmentToBranche.as_view(),name='newDepartmentToBranche'),
    path('<int:branche_id>/<int:departmnet_id>',DepartmentDetailsView.as_view(),name='DepartmentDetails'),
    path('<int:branche_id>/<int:departmnet_id>/EditDepartment',EditDepartmentToBranche.as_view(),name='EditDepartmentToBranche'),
    path('',include(router.urls)),
]