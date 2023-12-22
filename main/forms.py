from django.forms import ModelForm
from .models import Rawpacking


class RawpackingForm(ModelForm):
    class Meta:
        model = Rawpacking
        fields = '__all__'


