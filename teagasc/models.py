from django.db import models
from django.contrib.auth.models import User 
# User already defined in built in app named auth

counties = [
    ('1','Carlow'),
    ('2','Cavan'),
    ('3','Clare'),
    ('4','Cork'),
    ('5','Donegal'),
    ('6','Dublin'),
    ('7','Galway'),
    ('8','Kerry'),
    ('9','Kildare'),
    ('10','Kilkenny'),
    ('11','Laois'),
    ('12','Leitrim'),
    ('13','Limerick'),
    ('14','Longford'),
    ('15','Louth'),
    ('16','Mayo'),
    ('17','Meath'),
    ('18','Monaghan'),
    ('19','Offaly'),
    ('20','Roscommon'),
    ('21','Sligo'),
    ('22','Tipperary'),
    ('23','Waterford'),
    ('24','Westmeath'),
    ('25','Wexford'),
    ('26','Wicklow')]

class Farmer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    county = models.CharField(max_length=30,choices=counties,null=True)
    date = models.DateField(null=True)
    herd_no = models.IntegerField(null=True)

class Grassland(models.Model):
    owned_land = models.IntegerField(null=True)
    rented_land = models.IntegerField(null=True)
    total_grass_area = models.IntegerField(null=True)
    total_tillage_area = models.IntegerField(null=True)
    area_reseeded = models.IntegerField(null=True)
    
    organicN = models.IntegerField(null=True)
    organicP = models.IntegerField(null=True)
    type_of_stock = models.CharField(max_length=30,null=True)
    grassland_stocking_rate = models.IntegerField(null=True)
    soil_samples = models.CharField(max_length=30)
    reseeding = models.CharField(max_length=30)
    lime_required = models.IntegerField(null=True)
    enterprise = models.CharField(max_length=30)
    imports = models.IntegerField(null=True)
    exports = models.IntegerField(null=True)
    concentrateFed = models.IntegerField(null=True)
    legalN_limit = models.IntegerField(null=True)
    legalP_limit = models.IntegerField(null=True)

class Importation(models.Model):
    importation_original_stocking_rate = models.IntegerField(null=True)
    nitrates_and_potassium_figures = models.IntegerField(null=True)
    organic_manure_breakdown = models.IntegerField(null=True)
    exportation_details = models.CharField(max_length=30)
    stocking_rate_including_import = models.IntegerField(null=True)

class Exportation(models.Model):
    exportation_original_stocking_rate = models.IntegerField(null=True)
    export = models.IntegerField(null=True)
    person_accepting_import = models.CharField(max_length=30)
    new_stocking_rate = models.IntegerField(null=True)

class Monthly_Livestock_Numbers(models.Model):
    monthly_livestock_numbers = models.CharField(max_length=30)
    type_of_animal = models.CharField(max_length=30)
    organic_nitrates = models.IntegerField(null=True)
    organic_potassium = models.IntegerField(null=True)

class Tillage(models.Model):
    tillage_year = models.DateTimeField(null=True)
    tillage_imports = models.IntegerField(null=True)
    area_tillage = models.IntegerField(null=True)
    area_grassland = models.IntegerField(null=True)
    organic_nitrates_applied = models.IntegerField(null=True)
    organic_phospherus_applied = models.IntegerField(null=True)
    applied_potassium = models.IntegerField(null=True)
    field = models.CharField(max_length=30)
    fertilizer_allowed = models.IntegerField(null=True)

class Fertilzer_Plan(models.Model):
    opening_phospheros = models.IntegerField(null=True)
    opening_nitrogen = models.IntegerField(null=True)
    opening_stock = models.CharField(max_length=30)
    planned_purchases = models.CharField(max_length=30)
    lime = models.IntegerField(null=True)
    legally_allowed_nitrogen = models.IntegerField(null=True)
    legally_allowed_phospheros = models.IntegerField(null=True)

class Slurry_Storage(models.Model):
    storage_facility = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    number_of_tanks = models.IntegerField(null=True)
    type_of_tank = models.CharField(max_length=30)
    tank_dimensions = models.IntegerField(null=True)
    tank_capacity = models.IntegerField(null=True)
    enough_storage = models.IntegerField(null=True)

class Farm_Records(models.Model):
    farm_records_year = models.DateTimeField(null=True)
    farm_records_max_nitrogen_allowed = models.IntegerField(null=True)
    farm_records_max_phospheros_allowed = models.IntegerField(null=True)
    farm_records_opening_stock = models.CharField(max_length=30)
    fertilizer_bought = models.CharField(max_length=30)
    fertilizer_sold = models.CharField(max_length=30)
    closing_stock = models.CharField(max_length=30)
    total_usage = models.IntegerField(null=True)
    balance_under_recommended = models.IntegerField(null=True)
    balance_under_legal_amount = models.IntegerField(null=True)
    import_export_information = models.CharField(max_length=30)



