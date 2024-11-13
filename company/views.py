from django.shortcuts import render
from django.http import HttpResponse
from .models import Branches,Departments
from django.db import IntegrityError
from .form import addDepartmentToForm
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

def BranchesView(request):
   branches  = Branches.objects.all()
   return render(request,"company/BranchesList.html",{"branches":branches})

def BrancheDetailsView(request,branche_id):
   # branche = Branches.objects.get(id = branche_id)
   branche = Branches.objects.get(pk = branche_id)
   return render(request,"company/BrancheDetails.html",{"branche":branche})

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

def newDepartmentToBranche(request,branche_id):
   branche = Branches.objects.get(pk = branche_id)
   form = addDepartmentToForm()
   if request.method == 'POST':
      form = addDepartmentToForm(request.POST)
      if form.is_valid():
         if Departments.objects.filter(name = form.cleaned_data['name'],branche_id = branche_id).exists():
            form.add_error('name','this department is already exists in this branch')
            return render(request,'company/newDepartmentToBranche.html',{'form':form,'branche':branche})

         department = form.save(commit=False)
         department.branche_id = branche_id
         department.save()
         return render(request,"company/BrancheDetails.html",{"branche": branche})
      else:
         return render(request,"company/newDepartmentToBranche.html",{"branche":branche,"form":form})
   else:
      return render(request,"company/newDepartmentToBranche.html",{"branche":branche,"form":form})

# def view(request):
#    return HttpResponse("<h1>view 2</h1>")

# def editDepartmentToBranche(request,branche_id,depaertment_id):
#     form = editDepartmentToBrancheForm()
#     b = branches.objects.get(pk=branche_id)
#     dept = departments.objects.get(pk=depaertment_id)
#     form.fields['name'].initial = dept.name
#     form.fields['description'].initial = dept.description
#     if request.method == "POST":
#         form = editDepartmentToBrancheForm(request.POST)
#         if form.is_valid():
#             deptformData = form.save(commit=False)
#             dept.name = deptformData.name
#             dept.description = deptformData.description
#             dept.save()
#             return render(request,'company/brancheDetails.html',{'branche':b})
#     return render(request,'company/editDepartmentToBranche.html',{'form':form,'branche':b,'dept':dept})