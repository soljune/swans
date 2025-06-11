from django import forms
from .models import SwimWorkout, Pool

class SwimWorkoutForm(forms.ModelForm):
    class Meta:
        model = SwimWorkout
        fields = ['date', 'distance_meters', 'duration_minutes', 'stroke_type', 'notes']
        widgets = {
            'date': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
            'distance_meters': forms.NumberInput(attrs={'class': 'form-control'}),
            'duration_minutes': forms.NumberInput(attrs={'class': 'form-control'}),
            'stroke_type': forms.Select(attrs={'class': 'form-select'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }

class PoolForm(forms.ModelForm):
    class Meta:
        model = Pool
        fields = ['address', 'open_time', 'close_time', 'entry_price',
                  'has_changing_room', 'has_restaurant', 'has_parking', 'notes']
        widgets = {
            'address': forms.TextInput(attrs={'class': 'form-control'}),
            'open_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'close_time': forms.TimeInput(attrs={'class': 'form-control', 'type': 'time'}),
            'entry_price': forms.NumberInput(attrs={'class': 'form-control'}),
            'notes': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
        }
