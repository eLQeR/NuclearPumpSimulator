from django import forms
from .models import PumpLog, Pump

class PumpForm(forms.ModelForm):
    class Meta:
        model = PumpLog
        fields = ['pressure', 'temperature', 'performance',
                  'power', 'rotation_speed', 'pump', 'is_wheel_rotating', 'valve_status']


class PumpControlForm(forms.ModelForm):
    class Meta:
        model = Pump
        fields = ['status', 'serial_number', 'wanted_performance', 'wanted_rotation_speed']
        widgets = {
            'status': forms.Select(attrs={
                'class': 'form-select',
                'aria-label': 'Select status'
            }),
            'serial_number': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Serial Number'
            }),
            'wanted_performance': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Desired Performance (l/s)',
                'min': 0,
                'step': 0.1
            }),
            'wanted_rotation_speed': forms.NumberInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Desired Rotation Speed (RPM)',
                'min': 0,
                'step': 1
            }),
        }
        labels = {
            'status': 'Status',
            'serial_number': 'Serial Number',
            'wanted_performance': 'Desired Performance (l/s)',
            'wanted_rotation_speed': 'Desired Rotation Speed (RPM)',
        }