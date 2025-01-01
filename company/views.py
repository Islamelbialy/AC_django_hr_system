from typing import Any
from django.db.models.query import QuerySet
from django.forms import BaseModelForm
from django.shortcuts import render,redirect
from django.http import HttpRequest, HttpResponse
from .models import Branches,Departments
from django.db import IntegrityError
from .form import addDepartmentToForm
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView,CreateView
from django.urls import reverse_lazy
from rest_framework import viewsets
from .serializers import BranchesSerializer
# Create your views here.



# def BranchesView(request):
#    branches  = Branches.objects.all()
#    htmlSTR = """
#    <table>
#       <thead>
#          <th>name</th>
#          <th>address</th>
#          <th>email</th>
#       </thead>
#    """
#    for branche in branches:
#       htmlSTR += f"""
#          <tr>
#             <td>{branche.name}</td>
#             <td>{branche.address}</td>
#             <td>{branche.email}</td>
#          </tr>
#       """
   
#    htmlSTR += "</table>"

#    return HttpResponse(htmlSTR)

# def BranchesView(request):
#    branches  = Branches.objects.all()
#    return render(request,"company/BranchesList.html",{"branches":branches})

class BranchesView(ListView):
   model = Branches
   template_name = "company/BranchesList.html"
   context_object_name = 'branches'
   paginate_by = 5


# def BrancheDetailsView(request,branche_id):
#    # branche = Branches.objects.get(id = branche_id)
#    branche = Branches.objects.get(pk = branche_id)
#    return render(request,"company/BrancheDetails.html",{"branche":branche})

class BrancheDetailsView(ListView):
   template_name = "company/BrancheDetails.html"
   context_object_name = 'branche'

   def get_queryset(self):
      return Branches.objects.get(pk=self.kwargs["branche_id"])




# def DepartmentDetailsView(request,branche_id,departmnet_id):
#    branche = Branches.objects.get(pk = branche_id)
#    department = Departments.objects.get(pk = departmnet_id)
#    return render(request,"company/DepartmentsDetails.html",{"branche":branche,"departmnet":department})

class DepartmentDetailsView(ListView):
   template_name = "company/DepartmentsDetails.html"
   context_object_name = 'branche'

   def get_queryset(self):
      return Branches.objects.get(pk=self.kwargs["branche_id"])
   
   def get_context_data(self, **kwargs: Any) :
      context = super().get_context_data(**kwargs)
      context["departmnet"] = Departments.objects.get(pk = self.kwargs["departmnet_id"])
      return context

@login_required(login_url='/login/')
def newBrancheView(request):
   if request.method == 'POST':
      try:
         name = request.POST["brancheName"]
         address = request.POST["brancheAddress"]
         email = request.POST["brancheEmail"]
         Branches.objects.create(name = name,address = address,email = email)
      except IntegrityError as e:
         return render(request,"company/newBranche.html",{"err":"This entry already exists. "+ str(e)})
      except:
         return render(request,"company/newBranche.html",{"err":"error exists"})
   return render(request,"company/newBranche.html")

# def newDepartmentToBranche(request,branche_id):
#    branche = Branches.objects.get(pk = branche_id)
#    form = addDepartmentToForm()
#    if request.method == 'POST':
#       form = addDepartmentToForm(request.POST)
#       if form.is_valid():
#          if Departments.objects.filter(name = form.cleaned_data['name'],branche_id = branche_id).exists():
#             form.add_error('name','this department is already exists in this branch')
#             return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':branche})

#          department = form.save(commit=False)
#          department.branche_id = branche_id
#          department.save()
#          return render(request,"company/BrancheDetails.html",{"branche": branche})
#       else:
#          return render(request,"company/newDepartmentToBranche.html",{"branche":branche,"form":form})
#    else:
#       return render(request,"company/newDepartmentToBranche.html",{"branche":branche,"form":form})

class newDepartmentToBranche(CreateView):
   form_class = addDepartmentToForm
   template_name = "company/newDepartmentToBranche.html"
   success_url = reverse_lazy('BrancheDetails')
   

   def get_context_data(self, **kwargs: Any):
      context = super().get_context_data(**kwargs)
      context["branche"] = Branches.objects.get(pk = self.kwargs["branche_id"])
      return context 
   
   def form_valid(self, form):
      if Departments.objects.filter(name = form.cleaned_data['name'],branche_id = self.kwargs["branche_id"]).exists():
            form.add_error('name','this department is already exists in this branch')
            return self.form_invalid(form)

      department = form.save(commit=False)
      department.branche_id = self.kwargs["branche_id"]
      department.save()
      return redirect("BrancheDetails",branche_id =  self.kwargs["branche_id"])


# def EditDepartmentToBranche(request,branche_id,departmnet_id):
#    branche = Branches.objects.get(pk = branche_id)
#    department = Departments.objects.get(pk = departmnet_id)
#    form = addDepartmentToForm()
#    form.fields['name'].initial = department.name
#    form.fields['phone'].initial = department.phone
#    form.fields['describtion'].initial = department.describtion
#    if request.method == 'POST':
#       form = addDepartmentToForm(request.POST)
#       if form.is_valid():
#          if Departments.objects.filter(name = form.cleaned_data['name'],branche_id = branche_id).exclude(pk = departmnet_id).exists():
#             form.add_error('name','this department is already exists in this branch')
#             return render(request,'company/EditDepartmentToBranche.html',{'form':form,"departmnet":department,'branche':branche})

#          FormDepartment = form.save(commit=False)
#          department.name = FormDepartment.name
#          department.phone = FormDepartment.phone
#          department.describtion = FormDepartment.describtion
#          department.save()
#          return render(request,"company/DepartmentsDetails.html",{"branche": branche,"departmnet":department})
#       else:
#          return render(request,"company/EditDepartmentToBranche.html",{"branche":branche,"departmnet":department,"form":form})
#    else:
#       return render(request,"company/EditDepartmentToBranche.html",{"branche":branche,"departmnet":department,"form":form})

# def view(request):
#    return HttpResponse("<h1>view 2</h1>")

class EditDepartmentToBranche(CreateView):
   form_class = addDepartmentToForm
   template_name = "company/EditDepartmentToBranche.html"

   def dispatch(self, request, *args, **kwargs):
      self.branch =  Branches.objects.get(pk = self.kwargs["branche_id"])
      self.dept = Departments.objects.get(pk = self.kwargs["departmnet_id"])
      return super().dispatch(request, *args, **kwargs)


   def get_context_data(self, **kwargs):
      context = super().get_context_data(**kwargs)
      context["branche"] = self.branch
      context["departmnet"] = self.dept
      return context
   
   def get_initial(self):
      dept = self.dept
      initial = super().get_initial()
      initial["name"] = dept.name
      initial["phone"] = dept.phone
      initial["describtion"] = dept.describtion
      return initial
   
   def form_valid(self, form):
      if Departments.objects.filter(name = form.cleaned_data['name'],branche_id = self.kwargs['branche_id']).exclude(pk = self.kwargs['departmnet_id']).exists():
            form.add_error('name','this department is already exists in this branch')
            return self.form_invalid()

      department = self.dept
      FormDepartment = form.save(commit=False)
      department.name = FormDepartment.name
      department.phone = FormDepartment.phone
      department.describtion = FormDepartment.describtion
      department.save()
      return redirect("DepartmentDetails",branche_id =  self.kwargs["branche_id"],departmnet_id = self.kwargs["departmnet_id"])

