from django import forms
from cycle.models import CyclistModel , EventModel

class cycforms(forms.ModelForm):
    class Meta:
        model=CyclistModel
        fields="__all__"

class eveforms(forms.ModelForm):
    class Meta:
        model=EventModel
        fields="__all__"