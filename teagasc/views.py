from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.response import TemplateResponse
from teagasc.models import (Farmer,Grassland,counties,
Monthly_Livestock_Numbers, Farmer_Livestock, 
Farmer_Feed, Feed_Types, Importation, Exportation)
from teagasc.forms import GrasslandForm,Grassland2,Grassland3, Grassland4, Grassland5, import_Export
from django.views.decorators.csrf import csrf_protect
from datetime import datetime
from dateutil.parser import parse
import ipdb


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
        address = form["farmer_address_line_1"].value() + " " + form["farmer_address_line_2"].value()
         + " " + form["farmer_address_line_3"].value(),
        date = parse(form["date"].value(), dayfirst = True).strftime("%Y-%m-%d"), 
        county = form["county"].value(), herd_no = form["herd_no"].value())

        farmer.save()
        request.session["farmer_id"] = farmer.id

        return redirect("/conductGrasslandAssessment2")
    return render(request, "conductGrasslandAssessment.html", {'form':GrasslandForm()})

def record5_calculations(owned,rented,time):
            time /= 12
            rounded_time = round(time,2)
            rented = rented * time
            rounded_rented = round(rented,2)
            owned += rounded_rented

            return owned

@csrf_protect
def conductGrasslandAssessment2(request):
    if request.method=="POST":
        form = Grassland2(request.POST)
        if form.is_valid():
            farmer = Farmer.objects.get(id = request.session.get("farmer_id"))
            landInfo = Grassland(farmer_id = farmer, owned_land = (owned := float(form["owned_land"].value())),
            rented_land = (rented := float(form["rented_land"].value())),
            time_rented = (time_r := int(form["time_rented"].value())),
            total_tillage_area = (tillage := float(form["total_tillage_area"].value())), 
            area_reseeded = float(form["area_reseeded"].value()),
            total_grass_area = (area := record5_calculations(owned,rented,time_r)),
            total_land_area = area + tillage)
            landInfo.save()
            request.session["grassland_id"] = landInfo.id
            return redirect("/conductGrasslandAssessment5")
        else:
            return render(request, "conductGrasslandAssessment2.html", {'form':Grassland2()})

    return render(request, "conductGrasslandAssessment2.html", {'form':Grassland2()})

@csrf_protect
def conductGrasslandAssessment3(request):
    if request.method=="POST":
        form = Grassland3(request.POST)

        grass = Grassland.objects.get(id = request.session.get("grassland_id"))

        grass.sample_code = form["sample_code"].value()
        grass.sample_area = form["sample_area"].value()
        grass.date_taken = (date := parse(form["date_taken"].value(), dayfirst = True)).strftime("%Y-%m-%d")
        grass.expiry_date = date.replace(year = date.year + 5)
        grass.ph = form["ph"].value()
        grass.lime_required = form["lime_required"].value()
        grass.p_value = form["p_value"].value()
        grass.k_value = form["k_value"].value()
        grass.save()

        return redirect("/conductGrasslandAssessment4")
    return render(request, "conductGrasslandAssessment3.html", 
    {'form':Grassland3})

@csrf_protect
def conductGrasslandAssessment4(request):
    if request.method=="POST":
        form = Grassland4(request.POST)

        # need to get a value to associate the feeds with for grassland table
        # possibly feed tonnage 
        farmer = Farmer.objects.get(id = request.session.get("farmer_id"))
        grass = Grassland.objects.get(id = request.session.get("grassland_id"))

        num_of_feed = Farmer_Feed(farmer_id = farmer,
            number_compound  = (num1 := float(form['number_compound'].value())),
            number_wheat = (num2 := float(form['number_wheat'].value())),
            number_maize = (num3 := float(form['number_maize'].value())),
            number_maize_germ = (num4 := float(form['number_maize_germ'].value())),
            number_oats = (num5 := float(form['number_oats'].value())),
            number_beat_pulps_molassed = (num6 := float(form['number_beat_pulps_molassed'].value())),
            number_beat_pulp_unmolassed = (num7 := float(form['number_beat_pulp_unmolassed'].value())),
            number_citrus_pulp = (num8 := float(form['number_citrus_pulp'].value())),
            number_maize_distiller = (num9 := float(form['number_maize_distiller'].value())),
            number_maize_gluten = (num10 := float(form['number_maize_gluten'].value())),
            number_copra = (num11 := float(form['number_copra'].value())),
            number_cotton_seed = (num12 := float(form['number_cotton_seed'].value())),
            number_palm_kernel = (num13 := float(form['number_palm_kernel'].value())),
            number_rapeseed = (num14 := float(form['number_rapeseed'].value())),
            number_soya_bean = (num15 := float(form['number_soya_bean'].value())),
            number_sunflower = (num16 := float(form['number_sunflower'].value())),
            number_peas = (num17 := float(form['number_peas'].value())),
            number_beans = (num18 := float(form['number_beans'].value())),
            number_soya_hulls = (num19 := float(form['number_soya_hulls'].value())),
            number_distillers_grain = (num20 := float(form['number_distillers_grain'].value())),
            number_lucerne = (num21 := float(form['number_lucerne'].value())))
        
        grass.feed_tonnage = (total := (num1 + num2 + num3 + num4 + num5 + num6 + num7 + num8 + num9 + num10 + num11 + num12 + num13 + num14 +num15 + num16 + num17 + num18 + num19 + num20 + num21))
        grass.save()
        num_of_feed.save()
        return redirect("/conductGrasslandAssessment5")
    results = Feed_Types.objects.all()
    form = Grassland4()
    form = list(zip(results, form))
    return render(request, "conductGrasslandAssessment4.html", {'form':form})

@csrf_protect
def conductGrasslandAssessment5(request):
    if request.method=="POST":
        form = Grassland5(request.POST) 

        farmer = Farmer.objects.get(id = request.session.get("farmer_id"))
        grass = Grassland.objects.get(id = request.session.get("grassland_id"))
        num_of_stock = Farmer_Livestock(farmer_id = farmer,
            number_dairy_cows = (num1 := float(form['number_dairy_cows'].value())),
            number_suckler_cows = (num2 := float(form['number_suckler_cows'].value())),
            number_cattle1 = (num3 := float(form['number_cattle1'].value())),
            number_cattle2 = (num4 := float(form['number_cattle2'].value())),
            number_cattle3 = (num5 := float(form['number_cattle3'].value())),
            number_mountain_ewe = (num6 := float(form['number_mountain_ewe'].value())),
            number_lowland_ewe = (num7 := float(form['number_lowland_ewe'].value())),
            number_mountain_hogget = (num8 := float(form['number_mountain_hogget'].value())),
            number_lowland_hogget = (num9 := float(form['number_lowland_hogget'].value())),
            number_goats = (num10 := float(form['number_goats'].value())),
            number_horse1 = (num11 := float(form['number_horse1'].value())),
            number_horse2 = (num12 := float(form['number_horse2'].value())))

        animal_list = [
            num1,
            num2,
            num3,
            num4,
            num5,
            num6,
            num7,
            num8,
            num9,
            num10,
            num11,
            num12
        ]
        total_nitrates = 0
        grass.number_of_animals = (total := (sum(animal_list)))
        nitrate_results = Monthly_Livestock_Numbers.objects.values_list('organic_nitrates', flat=True)
        for a, b in zip(animal_list, nitrate_results):
            total_nitrates += a * b
        grass.organicN = total_nitrates

        total_potassium = 0
        potass_results = Monthly_Livestock_Numbers.objects.values_list('organic_potassium', flat = True)
        for c,d in zip(animal_list,potass_results):
            total_potassium += c * d
        grass.organicP = total_potassium

        total_lsu = 0
        lsu_vals = Monthly_Livestock_Numbers.objects.values_list('lsu', flat = True)
        for a,b in zip(animal_list, lsu_vals):
            total_lsu += a * b
        grass.lsu = total_lsu
        
        
        num_of_stock.save()
        grass.save()
        return redirect("/grasslandReport")
    results = Monthly_Livestock_Numbers.objects.all()
    form = Grassland5()
    form = list(zip(results, form))
    return render(request, "conductGrasslandAssessment5.html", {'form':form})


@csrf_protect
def grasslandAssessmentResult(request):
    everything = Grassland.objects.filter(farmer_id = request.session.get("farmer_id"))
    list_for_result = []
    objects_to_update = []
    for row in everything:
        total_organic_n = row.organicN
        total_organic_p = row.organicP
        total_land_area = row.total_land_area
        total_grass_area = row.total_grass_area
        total_lsu = row.lsu

        gsr = total_organic_n / total_grass_area
        wfsr = total_organic_n / total_land_area

        row.grassland_stocking_rate = gsr
        row.wholefarm_stocking_rate = wfsr
        objects_to_update.append(row)
        list_for_result.append((total_organic_n,total_organic_p, total_land_area, round(gsr,2), round(wfsr,2), round(total_lsu,2)))
    
    # The objects_to_update list will these columns in the database 
    Grassland.objects.bulk_update(objects_to_update,["grassland_stocking_rate","wholefarm_stocking_rate"])
    Farmer.objects.filter(id = request.session.get("farmer_id")).update(is_assessed=True)
    return render(request, "grasslandReport.html", {'list_for_result':list_for_result})


@csrf_protect
def importExport(request):
    if request.method=="POST":
        form = import_Export(request.POST) 
        try:
            farmer_name = form["farmer_name"].value()
            herd_no = farmer_name.split("-")[1].strip()
            farmer = Farmer.objects.get(herd_no=herd_no)
            if farmer == None:
                raise Exception()
            request.session["farmer_id"] = farmer.id
        except:
            farmer_list = Farmer.objects.filter(is_assessed = True)
            farmer_list = [f"{farmer.name} - {farmer.herd_no}" for farmer in farmer_list]
            return render(request, "importExport.html", {'form':import_Export, 'farmer_list':farmer_list})

        grass = Grassland.objects.get(farmer_id = request.session.get("farmer_id"))
        farmer = Farmer.objects.get(id = request.session.get("farmer_id"))

        total_n = grass.organicN
        area = grass.total_land_area

        if form["option"].value() == "Import":
            farmer_import = Importation(farmer_id = farmer,
            farmyard_manure = (manure := int(form["farmyard_manure"].value())), 
            slurry = (slurry := int(form["slurry"].value())),
            nitrates = (nit := int((slurry * 5) + manure * 4.5)))
            total_n += nit
            grass.organicN = total_n
            orgN = grass.organicN
            orgN / area
            farmer_import.save()
            grass.save()

        elif form["option"].value() == "Export":
            farmer_export = Exportation(farmer_id = farmer,
            farmyard_manure = (manure := int(form["farmyard_manure"].value())), 
            slurry = (slurry := int(form["slurry"].value())),
            nitrates = (nit := int((slurry * 5) + manure * 4.5)))
            total_n -= nit
            grass.organicN = total_n
            orgN = grass.organicN
            orgN / area
            grass.save()
            farmer_export.save()
            
        return redirect("/importExportReport")
    farmer_list = Farmer.objects.filter(is_assessed = True)
    farmer_list = [f"{farmer.name} - {farmer.herd_no}" for farmer in farmer_list]
    return render(request, "importExport.html", {'form':import_Export, 'farmer_list':farmer_list})

@csrf_protect
def importExportReport(request):
    everything = Grassland.objects.filter(farmer_id = request.session.get("farmer_id"))
    list_for_result = []
    objects_to_update = []
    for row in everything:
        total_organic_n = row.organicN
        total_organic_p = row.organicP
        total_land_area = row.total_land_area

        gsr = row.grassland_stocking_rate
        wfsr = total_organic_n / total_land_area

        row.wholefarm_stocking_rate = wfsr
        objects_to_update.append(row)
        list_for_result.append((total_organic_n,total_organic_p, total_land_area, round(gsr,2), round(wfsr,2)))
    
    # The objects_to_update list will these columns in the database 
    Grassland.objects.bulk_update(objects_to_update,["grassland_stocking_rate","wholefarm_stocking_rate"])
    Farmer.objects.filter(id = request.session.get("farmer_id")).update(is_assessed=True)
    return render(request, "importExportReport.html", {'list_for_result':list_for_result})   