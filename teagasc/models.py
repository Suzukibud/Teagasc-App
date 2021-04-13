from django.db import models
from django.contrib.auth.models import User 
# User already defined in built in app named auth

counties = [
    ('carlow','Carlow'),
    ('cavan','Cavan'),
    ('clare','Clare'),
    ('cork','Cork'),
    ('donegal','Donegal'),
    ('dublin','Dublin'),
    ('galway','Galway'),
    ('kerry','Kerry'),
    ('kildare','Kildare'),
    ('kilkenny','Kilkenny'),
    ('laois','Laois'),
    ('leitrim','Leitrim'),
    ('limerick','Limerick'),
    ('longford','Longford'),
    ('louth','Louth'),
    ('mayo','Mayo'),
    ('meath','Meath'),
    ('monaghan','Monaghan'),
    ('offaly','Offaly'),
    ('roscommon','Roscommon'),
    ('sligo','Sligo'),
    ('tipperary','Tipperary'),
    ('waterford','Waterford'),
    ('westmeath','Westmeath'),
    ('wexford','Wexford'),
    ('wicklow','Wicklow')]

counties_with_attrs = {
    "carlow": ('Carlow',0.024,"a",16),
    "cavan" : ('Cavan',0.027,"d",22),
    "clare" : ('Clare',0.032,"b",18),
    "Cork" : ('Cork',0.037,"a",16),
    "Donegal" : ('Donegal',0.038,"c",20),
    "Dublin" : ('Dublin',0.017,"a",16),
    "Galway" : ('Galway',0.034,"b",18),
    "Kerry" : ('Kerry',0.045,"b",18),
    "Kildare" : ('Kildare',0.018,"a",16),
    "Kilkenny" : ('Kilkenny',0.023,"a",16),
    "Laois" : ('Laois',0.022,"a",16),
    "Leitrim" : ('Leitrim',0.033,"c",20),
    "Limerick" : ('Limerick',0.026,"b",18),
    "Longford" : ('Longford',0.023,"b",18),
    "Louth" : ('Louth',0.020,"b",18),
    "Mayo" : ('Mayo',0.040,"b",18),
    "Meath" : ('Meath',0.019,"b",18),
    "Monaghan" : ('Monaghan',0.023,"d",22),
    "Offaly" : ('Offaly',0.020,"a",16),
    "Roscommon" : ('Roscommon',26,"b",18),
    "Sligo" : ('Sligo',0.032,"b",18),
    "Tipperary" : ('Tipperary',0.027,"a",16),
    "Waterford" : ('Waterford',0.031,"a",16),
    "Westmeath" : ('Westmeath',0.021,"b",18),
    "Wexford" : ('Wexford',0.025,"a",16),
    "Wicklow" : ('Wicklow',0.033,"a",16)
}

feed_types = [
    ('1','straight'),
    ('2','compound')]

livestock_type = [
    ('15','Dairy Cow'),
    ('2','Suckler Cow'),
    ('3','Cattle (0-1 year old)'),
    ('4','Cattle (1-2 years old)'),
    ('5','Cattle > 2 years'),
    ('6','Mountain ewe & lambs'),
    ('7','Lowland ewe & lambs'),
    ('8','Mountain hogget'),
    ('9','Lowland hogget'),
    ('10','Goat'),
    ('11','Horse (>3 years old)'),
    ('12','Horse (2-3 years old)')]

class Farmer(models.Model):
    name = models.CharField(max_length=30)
    address = models.CharField(max_length=30)
    county = models.CharField(max_length=30,choices=counties,null=True)
    date = models.DateField(null=True)
    herd_no = models.CharField(max_length=30,null=True, unique = True)
    is_assessed = models.IntegerField(null=True, default=0)
    zone = models.CharField(max_length=30)
    
class Grassland(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    owned_land = models.FloatField(null=True)
    rented_land = models.FloatField(null=True)
    time_rented = models.IntegerField(null=True)
    total_grass_area = models.FloatField(null=True)
    total_tillage_area = models.FloatField(null=True)
    total_land_area = models.FloatField(null=True)
    area_reseeded = models.FloatField(null=True)
    sample_code = models.CharField(max_length=30,null=True)
    date_taken = models.DateField(null=True)
    expiry_date = models.DateField(null=True)
    sample_area = models.FloatField(null=True)
    ph = models.FloatField(null=True)
    lime_required = models.FloatField(null=True)
    p_value = models.FloatField(null=True)
    p_index = models.FloatField(null=True)
    k_value = models.FloatField(null=True)
    k_index = models.FloatField(null=True)
    organicN = models.FloatField(null=True)
    organicP = models.FloatField(null=True)
    type_of_stock = models.CharField(max_length=30,null=True)
    type_of_feed = models.CharField(max_length=30,null=True)
    feed_name = models.CharField(max_length=30,null=True)
    feed_tonnage = models.CharField(max_length=30,null=True)
    number_of_animals = models.CharField(max_length=30,null=True)
    grassland_stocking_rate = models.FloatField(null=True)
    wholefarm_stocking_rate = models.FloatField(null=True)
    soil_samples = models.CharField(max_length=30)
    reseeding = models.CharField(max_length=30)
    lime_required = models.FloatField(null=True)
    enterprise = models.CharField(max_length=30)
    imports = models.FloatField(null=True)
    exports = models.FloatField(null=True)
    concentrateFed = models.FloatField(null=True)
    legalN_limit = models.FloatField(null=True)
    legalP_limit = models.FloatField(null=True)
    lsu = models.FloatField(null=True)

class Importation(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    farmyard_manure = models.IntegerField(null=True)
    slurry = models.IntegerField(null=True)
    nitrates = models.IntegerField(null=True)
    phosphate = models.IntegerField(null=True)

class Exportation(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    farmyard_manure = models.IntegerField(null=True)
    slurry = models.IntegerField(null=True)
    nitrates = models.IntegerField(null=True)
    phosphate = models.IntegerField(null=True)

class Monthly_Livestock_Numbers(models.Model):
    monthly_livestock_numbers = models.TextField(null=True)
    type_of_animal = models.CharField(max_length=30)
    organic_nitrates = models.FloatField(null=True)
    organic_potassium = models.FloatField(null=True)
    lsu = models.FloatField(null=True)
    slurry_m3 = models.FloatField(null=True)
    manure_m3 = models.FloatField(null=True)
    

class Tillage(models.Model):
    tillage_year = models.DateTimeField(null=True)
    tillage_imports = models.FloatField(null=True)
    area_tillage = models.FloatField(null=True)
    area_grassland = models.FloatField(null=True)
    organic_nitrates_applied = models.FloatField(null=True)
    organic_phospherus_applied = models.FloatField(null=True)
    applied_potassium = models.FloatField(null=True)
    field = models.CharField(max_length=30)
    fertilizer_allowed = models.FloatField(null=True)

class Fertilzer_Plan(models.Model):
    opening_phospheros = models.FloatField(null=True)
    opening_nitrogen = models.FloatField(null=True)
    opening_stock = models.CharField(max_length=30)
    planned_purchases = models.CharField(max_length=30)
    lime = models.FloatField(null=True)
    legally_allowed_nitrogen = models.FloatField(null=True)
    legally_allowed_phospheros = models.FloatField(null=True)

class Slurry_Storage(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    length = models.FloatField(null=True)
    breadth = models.FloatField(null=True)
    height = models.FloatField(null=True)
    total_slurry_manure = models.FloatField(null=True)
    total_storage = models.FloatField(null=True)
    rainfall = models.FloatField(null=True)
    num_containers = models.IntegerField(null=True)
    

class Farm_Records(models.Model):
    farm_records_year = models.DateTimeField(null=True)
    farm_records_max_nitrogen_allowed = models.FloatField(null=True)
    farm_records_max_phospheros_allowed = models.FloatField(null=True)
    farm_records_opening_stock = models.CharField(max_length=30)
    fertilizer_bought = models.CharField(max_length=30)
    fertilizer_sold = models.CharField(max_length=30)
    closing_stock = models.CharField(max_length=30)
    total_usage = models.FloatField(null=True)
    balance_under_recommended = models.FloatField(null=True)
    balance_under_legal_amount = models.FloatField(null=True)
    import_export_information = models.CharField(max_length=30)

class Farmer_Livestock(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    number_dairy_cows = models.IntegerField(null=True)
    number_suckler_cows = models.IntegerField(null=True)
    number_cattle1 = models.IntegerField(null=True)
    number_cattle2 = models.IntegerField(null=True)
    number_cattle3 = models.IntegerField(null=True)
    number_mountain_ewe = models.IntegerField(null=True)
    number_lowland_ewe = models.IntegerField(null=True)
    number_mountain_hogget = models.IntegerField(null=True)
    number_lowland_hogget = models.IntegerField(null=True)
    number_goats = models.IntegerField(null=True)
    number_horse1 = models.IntegerField(null=True)
    number_horse2 = models.IntegerField(null=True)

class Feed_Types(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    feed_type = models.CharField(max_length=30)
    feed_name = models.CharField(max_length=40)
    kg_per_tonne_fed = models.FloatField(null=True)

class Farmer_Feed(models.Model):
    farmer_id = models.ForeignKey(Farmer, on_delete = models.CASCADE, default=1)
    number_compound = models.IntegerField(null=True)
    number_wheat = models.IntegerField(null=True)
    number_maize = models.IntegerField(null=True)
    number_maize_germ = models.IntegerField(null=True)
    number_oats = models.IntegerField(null=True)
    number_beat_pulps_molassed = models.IntegerField(null=True)
    number_beat_pulp_unmolassed = models.IntegerField(null=True)
    number_citrus_pulp = models.IntegerField(null=True)
    number_maize_distiller = models.IntegerField(null=True)
    number_maize_gluten = models.IntegerField(null=True)
    number_copra = models.IntegerField(null=True)
    number_cotton_seed = models.IntegerField(null=True)
    number_palm_kernel = models.IntegerField(null=True)
    number_rapeseed = models.IntegerField(null=True)
    number_soya_bean = models.IntegerField(null=True)
    number_sunflower = models.IntegerField(null=True)
    number_peas = models.IntegerField(null=True)
    number_beans = models.IntegerField(null=True)
    number_soya_hulls = models.IntegerField(null=True)
    number_distillers_grain = models.IntegerField(null=True)
    number_lucerne =  models.IntegerField(null=True)







