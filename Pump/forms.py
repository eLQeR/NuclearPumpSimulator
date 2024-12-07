from django import forms
from .models import Pump

class PumpForm(forms.ModelForm):
    class Meta:
        model = Pump
        fields = ['name', 'status', 'pressure', 'temperature', 'performance',
                  'power', 'rotation_speed', 'is_wheel_rotating', 'valve_status']


class PumpControlForm(forms.ModelForm):
    class Meta:
        model = Pump
        fields = ['is_wheel_rotating', 'rotation_speed', 'valve_status']
