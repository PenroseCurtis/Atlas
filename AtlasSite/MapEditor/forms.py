from django import forms

from MapDisplayer.models import Map

class MapForm(forms.Form):
	name = forms.CharField(label='Map Name', max_length=100)
	summary = forms.CharField(label='Map Summary', max_length=1000)
	full_link = forms.CharField(label='External Link', max_length=100)
	is_private = forms.BooleanField(label='Is Map Private?')
	
	
