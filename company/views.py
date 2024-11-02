from django.shortcuts import render
from django.http import HttpResponse
from .models import Branches
from django.db import IntegrityError

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
   return render(request,"BranchesList.html",{"branches":branches})

def BrancheDetailsView(request,branche_id):
   # branche = Branches.objects.get(id = branche_id)
   branche = Branches.objects.get(pk = branche_id)
   return render(request,"BrancheDetails.html",{"branche":branche})

def newBrancheView(request):
   if request.method == 'POST':
      try:
         name = request.POST["brancheName"]
         address = request.POST["brancheAddress"]
         email = request.POST["brancheEmail"]
         Branches.objects.create(name = name,address = address,email = email)
      except IntegrityError as e:
         return render(request,"newBranche.html",{"err":"This entry already exists. "+ str(e)})
      except:
         return render(request,"newBranche.html",{"err":"error exists"})
   return render(request,"newBranche.html")

def view(request):
   return HttpResponse("<h1>view 2</h1>")