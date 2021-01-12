from django import forms

class GrasslandForm(forms.Form):
    farmer_name = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_email = forms.EmailField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_1 = forms.CharField(max_length=30, required=True, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_2 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    farmer_address_line_3 = forms.CharField(max_length=30, widget = forms.TextInput(attrs={ "class":"formclass"}))
    date = forms.DateField(widget = forms.TextInput(attrs={ "class":"formclass"}))
    herd_no = forms.IntegerField(widget = forms.TextInput(attrs={ "class":"formclass"}))

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