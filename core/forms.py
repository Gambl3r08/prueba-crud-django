from django import forms
from django.forms import fields
from .models import cancion
class CancionForm(forms.ModelForm):
    class Meta:
        model = cancion
        fields =['nombre', 'autor', 'album', 'duracion', 'fechaLanzamiento']
