from django import forms

from .models import Publisher

class PublisherModelForm(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = [
            'name',
            'address',
            'city',
            'state_province',
            'country',
            'website'
        ]