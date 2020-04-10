from django import forms 
from .models import Sneaker, Wearing

class SneakerForm(forms.ModelForm):
	class Meta:
		model = Sneaker
		fields = ('name', 'year', 'designer')

class WearingForm(forms.ModelForm):
	class Meta:
		model = Wearing
		fields = ['date', 'wear']