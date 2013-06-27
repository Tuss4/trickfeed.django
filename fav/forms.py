from django import forms

class AddFav(forms.Form):
	name = forms.CharField()
	video = forms.CharField()
	date = forms.DateTimeField()