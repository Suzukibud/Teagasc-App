from django import forms
from django.conf import settings
from .models import counties, feed_types, livestock_type


class GrasslandForm(forms.Form):
    farmer_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_1 = forms.CharField(max_length=30, required=True, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_2 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_3 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    date = forms.DateField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    date.input_formats = "%d-%m-%Y"
    county = forms.CharField(label="Please select a County ", widget=forms.Select(choices=counties, attrs={ "class":"formclass", 'style':'width:276px'}), max_length=1)
    herd_no = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))

class Grassland2(forms.Form):
    owned_land = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    rented_land = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    time_rented = forms.IntegerField(widget = forms.TextInput(attrs={"class":"formclass"}))
    total_tillage_area = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    area_reseeded = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))

class Grassland3(forms.Form):
    sample_code = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    date_taken = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    sample_area = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    ph = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    lime_required = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    p_value = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    k_value = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    soil_type = forms.CharField(widget = forms.TextInput(attrs={ "class":"formclass"}))

class Grassland4(forms.Form):
    number_compound = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_wheat = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_maize = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_maize_germ = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_oats = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_beat_pulps_molassed = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_beat_pulp_unmolassed = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_citrus_pulp = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_maize_distiller = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_maize_gluten = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_copra = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_cotton_seed = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_palm_kernel = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_rapeseed = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_soya_bean = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_sunflower = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_peas = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_beans = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_soya_hulls = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_distillers_grain = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_lucerne =  forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)

class Grassland5(forms.Form):
    number_dairy_cows = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_suckler_cows = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_cattle1 = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_cattle2 = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_cattle3 = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_mountain_ewe = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_lowland_ewe = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_mountain_hogget = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_lowland_hogget = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_goats = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_horse1 = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)
    number_horse2 = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}),initial=0)

class import_Export(forms.Form):
    CHOICES = (( 1, 'Import'), (2,'Export'))
    option = forms.ChoiceField(choices = CHOICES)
    farmyard_manure = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    slurry = forms.FloatField(widget = forms.TextInput(attrs={ "class":"formclass"}))



    def clean(self):
        cleaned_data = super(GrasslandForm, self).clean()
        cleaned_data1 = super(Grassland2, self).clean()
        cleaned_data2 = super(Grassland3, self).clean()
        cleaned_data3 = super(Grassland4, self).clean()
        cleaned_data4 = super(Grassland5, self).clean()
        name = cleaned_data.get('farmer_name')
        farmer_email = cleaned_data.get('farmer_email')
        farmer_address_line_1 = cleaned_data.get('farmer_address_line_1')
        farmer_address_line_2 = cleaned_data.get('farmer_address_line_2')
        farmer_address_line_3 = cleaned_data.get('farmer_address_line_3')
        date = cleaned_data.get('date')
        herd_no = cleaned_data.get('herd_no')

        if not name and not farmer_email and not farmer_address_line_1 and not farmer_address_line_2 and not farmer_address_line_3 and not date and not herd_no:
            raise forms.ValidationError('These fields are required')