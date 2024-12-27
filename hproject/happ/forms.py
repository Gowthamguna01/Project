from django import forms

from happ.models import Bus

class BusForm(forms.ModelForm):
    class Meta:
        model = Bus
        fields = "__all__"