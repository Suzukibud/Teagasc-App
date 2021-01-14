from django import forms
from .models import counties

class GrasslandForm(forms.Form):
    farmer_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_1 = forms.CharField(max_length=30, required=True, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_2 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_3 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    date = forms.DateField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    county = forms.CharField(label="Please select a County ", widget=forms.Select(choices=counties), max_length=1)
    herd_no = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))

class Grassland2(forms.Form):
    owned_land = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    rented_land = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    total_grass_area = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    total_tillage_area = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    area_reseeded = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))

    def clean(self):
        cleaned_data = super(GrasslandForm, self).clean()
        name = cleaned_data.get('farmer_name')
        farmer_email = cleaned_data.get('farmer_email')
        farmer_address_line_1 = cleaned_data.get('farmer_address_line_1')
        farmer_address_line_2 = cleaned_data.get('farmer_address_line_2')
        farmer_address_line_3 = cleaned_data.get('farmer_address_line_3')
        date = cleaned_data.get('date')
        herd_no = cleaned_data.get('herd_no')

        if not name and not farmer_email and not farmer_address_line_1 and not farmer_address_line_2 and not farmer_address_line_3 and not date and not herd_no:
            raise forms.ValidationError('These fields are required')