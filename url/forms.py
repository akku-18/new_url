from django.forms import ModelForm
from .models import SURL
class surlform(ModelForm):
    class Meta:
        model = SURL
        fields = ['link']
