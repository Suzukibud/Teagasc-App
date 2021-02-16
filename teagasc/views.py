from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from teagasc.models import Farmer,Grassland,counties
from teagasc.forms import GrasslandForm,Grassland2,Grassland3, Grassland4, Grassland5
from django.views.decorators.csrf import csrf_protect
from datetime import datetime

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
        date = form["date"].value(), county = form["county"].value(), herd_no = form["herd_no"].value())
        farmer.save()
        request.session["farmer_id"] = farmer.id
        return redirect("/conductGrasslandAssessment2")
    return render(request, "conductGrasslandAssessment.html", {'form':GrasslandForm()})

@csrf_protect
def conductGrasslandAssessment2(request):
    if request.method=="POST":
        form = Grassland2(request.POST)
        farmer = Farmer.objects.get(id = request.session.get("farmer_id"))
        landInfo = Grassland(farmer_id = farmer, owned_land = (owned := int(form["owned_land"].value())),
        rented_land = (rented := int(form["rented_land"].value())),
        total_tillage_area = (tillage := int(form["total_tillage_area"].value())), 
        area_reseeded = int(form["area_reseeded"].value()),
        total_grass_area = (area := (owned + rented)),
        total_land_area = area + tillage)
        landInfo.save()
        return redirect("/conductGrasslandAssessment3")
    return render(request, "conductGrasslandAssessment2.html", {'form':Grassland2()})

@csrf_protect
def conductGrasslandAssessment3(request):
    if request.method=="POST":
        form = Grassland3(request.POST)
        grass3 = Grassland(sample_code = form["sample_code"].value(),
        date_taken = form["date_taken"].value(),
        sample_area = form["sample_area"].value(),
        ph = form["ph"].value(),
        lime_required = form["lime_required"].value(),
        p_value = form["p_value"].value(),
        k_value = form["k_value"].value())
        grass3.save()
        return redirect("/conductGrasslandAssessment4")
    return render(request, "conductGrasslandAssessment3.html", 
    {'form':Grassland3})

@csrf_protect
def conductGrasslandAssessment4(request):
    if request.method=="POST":
        form = Grassland4(request.POST)
        grass4 = Grassland(type_of_feed = form["type_of_feed"].value(),
        feed_name = form["feed_name"].value(),
        feed_tonnage = form["tonnage"].value())
        grass4.save()
        return redirect("/conductGrasslandAssessment5")
    return render(request, "conductGrasslandAssessment4.html", 
    {'form':Grassland4})

@csrf_protect
def conductGrasslandAssessment5(request):
    if request.method=="POST":
        form = Grassland5(request.POST)
        grass5 = Grassland(type_of_stock = form["type_of_animal"].value(),
        number_of_animals = form["number_of_animals"].value())
        grass5.save()
    return render(request, "conductGrasslandAssessment5.html", 
    {'form':Grassland5})


@csrf_protect
def grasslandAssessmentResult(request):
    pass

# Create your views here.
## expiry_date = form["expiry_date"].value(),
#   k_index = form["k_index"].value()
