"""
URL configuration for hrsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from company import views as companyViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',companyViews.BranchesView,name='Branches'),
    path('<int:branche_id>/',companyViews.BrancheDetailsView,name='BrancheDetails'),
    path('view/',companyViews.view,name='viewURL'),
]
