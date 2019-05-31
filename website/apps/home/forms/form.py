from django import forms
from django.forms import widgets
from planificacion.models import *

class planificacionGeocercaForm(forms.ModelForm):
    class Meta:
        model = PlanificacionGeocerca
        fields = ('codigo','nombre','direccion','tipo_geocerca','coordenadas')

        widgets = {
            # 'is_miperfil': forms.RadioSelect(
            #    attrs={
            #        'class':'cssRadio'
            #    }
            # ),
            'coordenadas': forms.HiddenInput(
                attrs={
                    'value': '{}',
                    'class': 'form-control',
                }
            ),
            'codigo': forms.TextInput(
                attrs={
                    'required': True,
                    'value': '',
                    'class': 'form-control',
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'required': True,
                    'value': '',
                    'class': 'form-control',
                }
            ),
            'direccion': forms.TextInput(
                attrs={
                    'required': True,
                    'value': '',
                    'class': 'form-control',
                }
            ),
            'tipo_geocerca': forms.Select(
                attrs={
                    'required': False,
                    'value': '',
                    'class': 'form-control',
                }
            ),
        }


class MyForm(forms.Form):
    LABEL_TIPO_DOCUMENTO = u'Seleccione Tipo de Documento.'

    """department = forms.ModelChoiceField(
        widget=forms.Select(
            attrs={'departament_id'}),
        queryset=None, empty_label=LABEL_DEPARTMENT)"""


    #otroppago_numdoc = forms.CharField(max_length=16,widget=forms.fields.TextInput(
    #        attrs={'placeholder': 'Número de documento'}))
    #otroppago_nombre = forms.CharField(max_length=128)
    #otroppago_apepat = forms.CharField(max_length=128)
    #otroppago_apemat = forms.CharField(max_length=128)
    #otroppago_email = forms.CharField(max_length=128)
    #otroppago_telefono = forms.CharField(max_length=16)

    MY_CHOICES = (
        ('DNI', 'DNI'),
        ('CEX', 'Carné extranjeria'),
        ('CDI', 'Carné de diplomático')
    )

    otroppago_tipodoc2 = forms.ChoiceField(
        widget=forms.Select(
            attrs={'class': 'sel-field', 'tabindex': '9'})
    )
    otroppago_numdoc = forms.CharField(
        #required=True,
        widget=forms.fields.TextInput(
            attrs={'placeholder': 'Número de documento', 'class': 'text-field num-doc' , 'tabindex': '10'})
    )
    otroppago_nombre = forms.CharField(
        max_length=128,
        #required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Escriba su nombre completo', 'class': 'text-field', 'tabindex': '11', 'onkeypress': 'return soloLetras(event)',})
    )
    otroppago_apepat = forms.CharField(
        max_length=128,
        #required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Escriba su apellido paterno', 'class': 'text-field', 'tabindex': '12', 'onkeypress': 'return soloLetras(event)',})
    )
    otroppago_apemat = forms.CharField(
        max_length=128,
        #required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Escriba su apellido materno', 'class': 'text-field', 'tabindex': '13', 'onkeypress': 'return soloLetras(event)',})
    )
    otroppago_email = forms.CharField(
        max_length=128,
        #required=True,
        widget=forms.TextInput(
            attrs={'type': 'email', 'placeholder': 'Escriba su correo', 'class': 'text-field', 'tabindex': '15'}),
    )
    otroppago_telefono = forms.CharField(
        max_length=16,
        #required=True,
        widget=forms.TextInput(
            attrs={'placeholder': 'Escriba su Teléfono', 'class': 'text-field', 'tabindex': '14'}),
    )

    otroppago_is_miperfil = forms.CharField(
        required=False,
        widget=forms.CheckboxInput(
            attrs={
            'type': 'checkbox', 'value': 0, 
        }),
    )