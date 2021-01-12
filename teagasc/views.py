from django.shortcuts import render
from django.http import HttpResponse
from django.template.response import TemplateResponse
from teagasc.models import Farmer
from teagasc.forms import GrasslandForm
from django.views.decorators.csrf import csrf_protect

def home(request):
    #e = Exportation(exportation_original_stocking_rate = 15,
    #export = 20, person_accepting_import = "MIchael", new_stocking_rate = 20)
    #e.save()
    return TemplateResponse(request, "home.html")

@csrf_protect
def conductAssessment(request):
    if request.method=="POST":
        form = GrasslandForm(request.POST)
        farmer = Farmer(name = form["farmer_name"].value(),
        location = form["farmer_address_line_1"].value() + form["farmer_address_line_2"].value() + form["farmer_address_line_3"].value(),
        year = "2020-12-12", herd_no = form["herd_no"].value(), type_of_stock="cows", land="yes")
        farmer.save()
    return render(request, "conductAssessment.html", {'form':GrasslandForm()})


# Create your views here.
