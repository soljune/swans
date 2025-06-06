from django import forms
from .models import SwimWorkout,Pool

class SwimWorkoutForm(forms.ModelForm):
    class Meta:
        model = SwimWorkout
        fields = ['date', 'distance_meters', 'duration_minutes', 'stroke_type', 'notes']

class PoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['address', 'open_time', 'close_time', 'entry_price',
                 'has_changing_room', 'has_restaurant', 'has_parking', 'notes']
        widgets = {
        'input_field': forms.TextInput(attrs={'class': 'form-control'}),
        'textarea_field': forms.Textarea(attrs={'class': 'form-control'}),
        'date_field': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
    }