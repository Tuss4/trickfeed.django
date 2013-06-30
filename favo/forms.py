from django import forms

class AddFav(forms.Form):
	video = forms.CharField()