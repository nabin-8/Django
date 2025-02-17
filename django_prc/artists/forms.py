from django import forms
from .models import Artist

class ArtistForm(forms.ModelForm):
    class Meta:
        model = Artist
        fields:['name', 'dob', 'gender', 'address', 'first_release_year', 'no_of_albums_released']
        widgets = {
            'dob': forms.DateInput(attrs={'type': 'date'}),
        }