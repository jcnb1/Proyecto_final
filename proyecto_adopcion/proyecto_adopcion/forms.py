from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Mascota
from proyecto_adopcion.adopcion.models import Persona

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    password1 = forms.CharField(label = 'Contraseña', widget = forms.PasswordInput)
    password2 = forms.CharField(label = 'Confirma Contraseña', widget = forms.PasswordInput)



class MascotaForm(forms.ModelForm):

    class Meta:
        model = Mascota

        fields = [
            'tipo_mascota'
            'nombre'
            'sexo'
            'edad_aproximada'
            'fecha_rescate'
            'descripcion'
            'persona'
            'vacuna'
        ]
        labels = {
            'tipo_mascota': 'Tipo de Mascota',
            'nombre': 'Nombre',
            'sexo': 'Sexo',
            'edad_aproximada': 'Edad aproximada',
            'fecha_rescate': 'Fecha de rescate',
            'persona': 'Candidatos',
            'vacuna': 'Vacunas',
        }
        widgets = {
            'tipo_mascota': forms.TextInput(attrs={'class':'form-control'}),
            'nombre': forms.TextInput(attrs={'class':'form-control'}),
            'sexo': forms.TextInput(attrs={'class':'form-control'}),
            'edad_aproximada': forms.TextInput(attrs={'class':'form-control'}),
            'fecha_rescate': forms.TextInput(attrs={'class':'form-control'}),
            'persona': form.Select(attrs={'class':'form-control'}),
            'vacuna': forms.CheckboxSelectMultiple(),
        }