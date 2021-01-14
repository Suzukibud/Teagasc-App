from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from teagasc.models import Farmer
from teagasc.models import Grassland
from teagasc.models import counties
from teagasc.forms import GrasslandForm
from teagasc.forms import Grassland2
from django.views.decorators.csrf import csrf_protect

def home(request):
    #e = Exportation(exportation_original_stocking_rate = 15,
    #export = 20, person_accepting_import = "MIchael", new_stocking_rate = 20)
    #e.save()
    return TemplateResponse(request, "home.html")

@csrf_protect
def conductGrasslandAssessment(request):
    if request.method=="POST":
        form = GrasslandForm(request.POST)
        farmer = Farmer(name = form["farmer_name"].value(),
        address = form["farmer_address_line_1"].value() + " " + form["farmer_address_line_2"].value() + " " + form["farmer_address_line_3"].value(),
        date = "2020-12-12", herd_no = form["herd_no"].value(), county = form["county"].value())
        farmer.save()
    return render(request, "conductGrasslandAssessment.html", {'form':GrasslandForm()})

@csrf_protect
def conductGrasslandAssessment2(request):
    if request.method=="POST":
        form = Grassland2(request.POST)
        landInfo = Grassland(owned_land = form["owned_land"].value(),
        rented_land = form["rented_land"].value(),
        total_grass_area = form["total_grass_area"].value(), 
        total_tillage_area = form["total_tillage_area"].value(), 
        area_reseeded = form["area_reseeded"].value())
        landInfo.save()
    return render(request, "conductGrasslandAssessment2.html", {'form':Grassland2()})

# Create your views here.
