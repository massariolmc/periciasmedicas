from django.forms import ModelForm, TextInput, Textarea, DateInput, Select, SelectDateWidget, HiddenInput, DateTimeInput, EmailInput
from django import forms
from .models import MedicalSpecialty, PersonType, Person, ProfilePersonType, Doctor, MedicalSpecialty, DoctorList
from PericiasMedicas.company.models import Company,Department
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML, Hidden, Field
from django.core.exceptions import ValidationError

class PersonForm(ModelForm):

    class Meta:
        model = Person        
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'dt_birthday': DateInput(format='%d/%m/%Y', attrs={'class': 'form-control calendario'}),
            'cpf': TextInput(attrs={'class': 'form-control cpf','onkeypress':'return somenteNumeros(event)'}),
            'sex': Select(attrs={'class': 'form-control'}),
            'uf_natural': TextInput(attrs={'class': 'form-control cidade_estado'}),
            'maritalstatus': Select(attrs={'class': 'form-control'}),
            'rg': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'rg_exped': TextInput(attrs={'class': 'form-control'}),
            'rg_uf': Select(attrs={'class': 'form-control'}),
            'pis_pasep': TextInput(attrs={'class': 'form-control ','onkeypress':'return somenteNumeros(event)'}),
            'voter_title_num': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'voter_title_section': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'voter_title_zone': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'voter_title_uf': Select(attrs={'class': 'form-control'}),
            'cnh_num': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'cnh_uf': Select(attrs={'class': 'form-control'}),
            'cnh_validate': DateInput(format='%d/%m/%Y', attrs={'class': 'form-control calendario'}),
            'cnh_category': Select(attrs={'class': 'form-control'}),            
            'address': TextInput(attrs={'class': 'form-control'}),
            'address_num': TextInput(attrs={'class': 'form-control'}),
            'address_city_uf': TextInput(attrs={'class': 'form-control cidade_estado'}),
            'cep': TextInput(attrs={'class': 'form-control cep','onkeypress':'return somenteNumeros(event)'}),
            'email': EmailInput(attrs={'class': 'form-control'}),            
            'phone': TextInput(attrs={'class': 'form-control phone','onkeypress':'return somenteNumeros(event)'}),
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),
            #SO, IP e BROWSER serão direto na view
        }
        error_messages = {
            'name': {
                'blank': ("Não pode ser em branco."),
            },
        }

class PersonTypeForm(ModelForm):

    class Meta:
        model = PersonType
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),            
            'name',                                               
            HTML('''
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_departments_list'%}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class ProfilePersonTypeForm(ModelForm):      

    search_person = forms.CharField(label="Pessoa Find", max_length=100, required=True, 
                    widget=forms.TextInput(attrs={'placeholder': 'Digite um nome...'}))  
    class Meta:
        model = ProfilePersonType
        fields = '__all__'
        #fields = ['person','person_type', 'department', 'user_created','user_updated','select_company','search_person']
        widgets = {
            'person': HiddenInput(attrs={'class': 'form-control'}),
            'person_type': Select(attrs={'class': 'form-control'}),
            'department': Select(attrs={'class': 'form-control'}),
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
    
    def __init__(self, *args, **kwargs):         
        self.person_name = kwargs.get('person_name','')# faz parte do edit do profile person type
        self.person_id = kwargs.get('person_id','')# faz parte do edit do profile person type   
        if self.person_name and self.person_id:
            del(kwargs['person_name'])# faz parte do edit do profile person type
            del(kwargs['person_id'])# faz parte do edit do profile person type               
        super().__init__(*args, **kwargs)    
        self.helper = FormHelper()
        print("person name do init", self.person_name)
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),            
            Hidden('person',self.person_id),           
            Hidden('department','{{ department_id }}'),
            #'search_person',
            Field('search_person', value=self.person_name),
            'person_type',                                                                       
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_profilepersontypes_list' department_id%}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class MedicalSpecialtyForm(ModelForm):
    class Meta:
        model = MedicalSpecialty
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),            
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
    
    #VALIDAÇÃO
    def clean_name(self):        
        name = self.cleaned_data['name']
        if self.instance.id:
            n = MedicalSpecialty.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists()#Verifica se o nome já existe            
        else:
            n = MedicalSpecialty.objects.filter(name__iexact=name).exists()#Verifica se o nome já existe                
        if n:            
            raise ValidationError("Especialidade já cadastrada. Informe outra.")
        return name

    def __init__(self, *args, **kwargs):                        
        super().__init__(*args, **kwargs)    
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),                      
            'name',                                                                       
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_medicalspecialties_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class DoctorForm(ModelForm):
    #A linha abaixo serve para sobreescrever os valores que vão aparecer no Select do profile person type
    profile_person_type = forms.ModelChoiceField(label="Perito",queryset=ProfilePersonType.objects.filter(person_type_id=3), empty_label="SELECIONE")
    
    class Meta:
        model = Doctor
        fields = '__all__'
        widgets = {
            'crm_num': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'crm_uf': Select(attrs={'class': 'form-control'}),
            'course': Textarea(attrs={'class': 'form-control'}),
            'medical_specialty': Select(attrs={'class': 'form-control'}),
            'profile_person_type': Select(attrs={'class': 'form-control'}),                     
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
    
    #VALIDAÇÃO
    def clean_profile_person_type(self):        
        name = self.cleaned_data['profile_person_type']
        ms = self.cleaned_data['medical_specialty']
        if self.instance.id:
            n = Doctor.objects.filter(profile_person_type=name, medical_specialty=ms).exclude(id=self.instance.id).exists()#Verifica se o nome já existe            
        else:
            n = Doctor.objects.filter(profile_person_type=name, medical_specialty=ms).exists()#Verifica se o nome já existe                
        if n:            
            raise ValidationError("Perito já cadastrado nesta especialidade.")
        return name

    def __init__(self, *args, **kwargs):                        
        super().__init__(*args, **kwargs)        
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),                      
            'profile_person_type',
            'medical_specialty',
            'course',
            'crm_num',
            'crm_uf',                                                                       
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_doctors_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class DoctorListForm(ModelForm):
    class Meta:
        model = DoctorList
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'crm': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'state': Select(attrs={'class': 'form-control'}),            
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
    
    #VALIDAÇÃO
    def clean_crm(self):        
        crm = self.cleaned_data['crm']
        if self.instance.id:
            n = DoctorList.objects.filter(crm__iexact=crm).exclude(id=self.instance.id).exists()#Verifica se o crm já existe            
        else:
            n = DoctorList.objects.filter(crm__iexact=crm).exists()#Verifica se o crm já existe                
        if n:            
            raise ValidationError("CRM já cadastrada. Informe outra.")
        return crm

    def __init__(self, *args, **kwargs):                        
        super().__init__(*args, **kwargs)    
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),                      
            'name',
            'crm',
            'state',                                                                       
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_doctorlists_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )



