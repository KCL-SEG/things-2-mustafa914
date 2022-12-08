"""Forms of the project."""
from django import forms
from django.core.validators import RegexValidator
from things.models import Thing

class ThingForm(forms.ModelForm):
    class Meta:
        model = Thing
        fields = ['name', 'description', 'quantity']
        widgets = {'description': forms.Textarea}

    def clean(self):
        """Cleans the data and rejects invalid inputs"""
        super().clean()

    def save(self):
        super().save()
        thing = Thing.objects.create(
            name = self.cleaned_data.get('name'),
            description = self.cleaned_data.get('description'),
            quantity = self.cleaned_data.get('quantity'),
        )
        return thing

