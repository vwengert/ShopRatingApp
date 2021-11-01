from django import forms

from .models import Shop, Rating

class ShopForm(forms.ModelForm):
    class Meta:
        model = Shop
        fields = ['name']
        labels = {'name': ''}

class RatingForm(forms.ModelForm):
    class Meta:
        model = Rating
        fields = ['rating', 'description']
        labels = {'rating': 'Bewertung', 'description': 'Beschreibung'}
        widgets = {'description': forms.Textarea(attrs={'cols': 80})}
