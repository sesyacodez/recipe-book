from django import forms
from .models import Recipe


class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = [
            'title',
            'description',
            'instructions',
            'cuisine',
            'ingredients',
            'categories',
        ]
        widgets = {
            'ingredients': forms.CheckboxSelectMultiple,
            'categories': forms.CheckboxSelectMultiple,
        }
