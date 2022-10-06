from django import forms

class form_user(forms.Form):
    name = forms.CharField(max_length=30)
    lastName = forms.CharField(max_length=30)
    email = forms.EmailField()

#class form_driver(forms.Form):
#    name = forms.CharField(max_length=30)
#    lastName = forms.CharField(max_length=30)
#    email = forms.EmailField()
#    registry = forms.IntegerField()

#class form_movile(forms.Form):
#    carPatent = forms.CharField(max_length=30)
#    carBrand = forms.CharField(max_length=30)
#    year = forms.IntegerField()