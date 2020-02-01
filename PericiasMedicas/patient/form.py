from django.forms import ModelForm, TextInput, DateInput, FileInput, Select, SelectDateWidget, HiddenInput, DateTimeInput
from .models import Patients
from django.utils.translation import gettext_lazy as _


class PatientForm(ModelForm):

    class Meta:
        model = Patients
        #fields = ['name','dt_birthday', 'rg', 'rg_exped', 'rg_uf','cpf', 'name_mother', 'name_father', 'sex', 'uf_natural', 'origin', 'schooling','maritalstatus', 'religion', 'situation_inss', 'scort', 'email']
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'dt_birthday': DateTimeInput(format='%d/%m/%Y %H:%M', attrs={'class': 'form-control calendario'}),
            'rg': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'rg_exped': TextInput(attrs={'class': 'form-control'}),
            'rg_uf': Select(attrs={'class': 'form-control'}),
            'cpf': TextInput(attrs={'class': 'form-control cpf', 'onkeypress':'return somenteNumeros(event)'}),
            'name_mother': TextInput(attrs={'class': 'form-control'}),
            'name_father': TextInput(attrs={'class': 'form-control'}),
            'sex': Select(attrs={'class': 'form-control'}),
            'uf_natural': TextInput(attrs={'class': 'form-control cidade_estado'}),
            'origin': Select(attrs={'class': 'form-control'}),
            'schooling': Select(attrs={'class': 'form-control'}),
            'maritalstatus': Select(attrs={'class': 'form-control'}),
            'religion': Select(attrs={'class': 'form-control'}),
            'situation_inss': Select(attrs={'class': 'form-control'}),
            'scort': TextInput(attrs={'class': 'form-control'}),
            'scort_type': Select(attrs={'class': 'form-control'}),
            'email': TextInput(attrs={'class': 'form-control'}),            
            'blood_type': Select(attrs={'class': 'form-control'}),
            'blood_rh': Select(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'address_num': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'address_city_uf': TextInput(attrs={'class': 'form-control cidade_estado'}),
            'cep': TextInput(attrs={'class': 'form-control cep', 'onkeypress':'return somenteNumeros(event)'}),
            'phone': TextInput(attrs={'class': 'form-control phone'}),
            'user': HiddenInput(attrs={'class': 'form-control'}),
            'avatar': FileInput(attrs={'class': 'form-control'}),
        }
        error_messages = {
            'name': {
                'blank': _("Não pode ser em branco."),
            },
        }