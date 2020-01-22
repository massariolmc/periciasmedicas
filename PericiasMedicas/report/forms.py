from django.forms import ModelForm, TextInput, Textarea, DateInput, RadioSelect,Select, SelectDateWidget, HiddenInput, DateTimeInput, EmailInput
from django import forms
from pericias.person.models import MedicalSpecialty, PersonType, Person, ProfilePersonType, Doctor, MedicalSpecialty
from .models import AuthorityRequesting, ForensicScan, ReportStatus, Report, MedicalDocument, NatureOfAction, TypeItem, TypeItemByNatureOfAction, Item2
from pericias.company.models import Department, Company
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML, Hidden, Field
from django.core.exceptions import ValidationError
from ckeditor.fields import RichTextField
from ckeditor.fields import RichTextFormField
from ckeditor.widgets import CKEditorWidget

class AuthorityRequestingForm(ModelForm):    
    
    class Meta:
        model = AuthorityRequesting
        fields = '__all__'
        widgets = {
            'profile_person_type': Select(attrs={'class': 'form-control'}),
            'name': TextInput(attrs={'class': 'form-control'}),
            'abbreviation': TextInput(attrs={'class': 'form-control'}),                                
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  

    def __init__(self, *args, **kwargs):    
        #Serve para pegar qual Empresa pertence os peritos                   
        self.department_id = kwargs.get('department_id',None)                    
        del(kwargs['department_id'])                      
        super().__init__(*args, **kwargs)  
        #A linha abaixo serve para sobreescrever os valores que vão aparecer no Select do profile person type    
        self.fields['profile_person_type'].empty_label= "-----------"
        #Neste caso, preciso no seletec que apareça apenas os peritos da Empresa do usuário que está logado        
        self.fields['profile_person_type'].queryset = ProfilePersonType.objects.filter(department_id__in=self.department_id, person_type__name="Perito")              
        
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'), 
            'profile_person_type',                      
            'name',
            'abbreviation',                                                                                  
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_authorityrequesting_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class ForensicScanForm(ModelForm): 
    
    class Meta:
        model = ForensicScan
        fields = '__all__'
        widgets = {
            'profile_person_type': Select(attrs={'class': 'form-control'}),
            'nature_of_action': Select(attrs={'class': 'form-control'}),
            'version': TextInput(attrs={'class': 'form-control'}),
            'forensicscan': Textarea(attrs={'class': 'form-control'}),
            'goal': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_history': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_personal_background': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_family_background': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_general_exam': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_mental_exam': Textarea(attrs={'class': 'form-control'}),            
            'anamnesis_diagnosis': Textarea(attrs={'class': 'form-control'}),
            'cid_number': TextInput(attrs={'class': 'form-control'}),
            'discussion': Textarea(attrs={'class': 'form-control'}),
            'conclusion': Textarea(attrs={'class': 'form-control'}),                                           
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  
    
    def __init__(self, *args, **kwargs):     
        #Serve para pegar qual Empresa pertence os peritos                   
        self.department_id = kwargs.get('department_id',None)                    
        del(kwargs['department_id'])                 
        super().__init__(*args, **kwargs)           
        #A linha abaixo serve para sobreescrever os valores que vão aparecer no Select do profile person type    
        self.fields['profile_person_type'].empty_label= "ESCOLHA"
        #Neste caso, preciso no seletec que apareça apenas os peritos da Empresa do usuário que está logado
        #self.fields['profile_person_type'].queryset = ProfilePersonType.objects.filter(department__company_id=self.company_id, person_type=3)        
        self.fields['profile_person_type'].queryset = ProfilePersonType.objects.filter(department_id__in=self.department_id, person_type=3)                
        self.fields['nature_of_action'].empty_label= "ESCOLHA"      
        
class ReportStatusForm(ModelForm):    
    
    class Meta:
        model = ReportStatus
        fields = '__all__'
        widgets = {
            'status': TextInput(attrs={'class': 'form-control'}),                                           
            'obs': Textarea(attrs={'class': 'form-control'}),                                           
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  

    def __init__(self, *args, **kwargs):                        
        super().__init__(*args, **kwargs)        
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),                      
            'status',  
            'obs',                                                                                         
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_reportstatus_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class ReportForm(ModelForm):
    #A linha abaixo serve para sobreescrever os valores que vão aparecer no Select do profile person type    
    value_tab = forms.CharField(max_length=100, required=False)
        
    #O queryset do campo abaixo está sobreescrito no init. Só aparece opção para as pessoas daquele departamento que criaram um tipo de quesito por natureza de ação
    type_item_by_nature_of_action = forms.ModelChoiceField(label='Tipo de Quesito',queryset=TypeItemByNatureOfAction.objects.all(),empty_label="Escolha", required=False, widget=forms.Select(attrs={'class': 'form-control'}))    
    question = forms.CharField(label="Pergunta",widget=CKEditorWidget(),required=False)
    
    class Meta:
        model = Report
        fields = '__all__'
        widgets = {
            'authority_requesting': Select(attrs={'class': 'form-control'}),                                           
            'nature_of_action': Select(attrs={'class': 'form-control'}),
            'process_number': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'autor': Select(attrs={'class': 'form-control'}),
            'proficient': Select(attrs={'class': 'form-control'}),
            'date_report': DateInput(attrs={'class': 'form-control calendario'}),
            'profile_person_type': Select(attrs={'class': 'form-control'}),
            'forensic_scan': Select(attrs={'class': 'form-control'}),
            'anamnesis_history': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_personal_background': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_family_background': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_general_exam': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_mental_exam': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_medical_documents': Textarea(attrs={'class': 'form-control'}),
            'anamnesis_diagnosis': Textarea(attrs={'class': 'form-control'}),             
            'cid_number': TextInput(attrs={'class': 'form-control cid_number'}), 
            'discussion': Textarea(attrs={'class': 'form-control'}),
            'conclusion': Textarea(attrs={'class': 'form-control'}),                                           
            'report_status': Select(attrs={'class': 'form-control'}), 
            'obs': Textarea(attrs={'class': 'form-control'}),             
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),
            'value_tab': HiddenInput(attrs={'class': 'form-control'}),#APENAS SERVE PARA SABER QUAL TAB ESTÁ            
        }  

    def __init__(self, *args, **kwargs):     
        #Serve para pegar qual Empresa pertence os peritos                   
        self.department_id = kwargs.get('department_id',None)    
        self.user_id = kwargs.get('user_id',None)                
        del(kwargs['department_id'])
        del(kwargs['user_id'])
        super().__init__(*args, **kwargs)           
        #A linha abaixo serve para sobreescrever os valores que vão aparecer no Select do profile person type    
        self.fields['profile_person_type'].empty_label= "-----------"
        #Neste caso, preciso no seletec que apareça apenas os peritos da Empresa do usuário que está logado            
        self.fields['profile_person_type'].queryset = ProfilePersonType.objects.filter(department_id__in=self.department_id, person_type=3)        
        #Neste caso, preciso dsa circunstância deste perito. Cada perito tem sua circunstância.        
        if self.instance.pk:            
            self.fields['forensic_scan'].queryset = ForensicScan.objects.filter(profile_person_type__id=self.instance.profile_person_type.id, nature_of_action=self.instance.nature_of_action)                   
            #Aqui vai listar apenas quesitos que o usuário cadastrou e o tipo de natureza de ação que o Laudo possui
            self.fields['type_item_by_nature_of_action'].queryset = TypeItemByNatureOfAction.objects.filter(nature_of_action=self.instance.nature_of_action,type_item__user_created=self.user_id)
            

class MedicalDocumentForm(ModelForm):    
    
    class Meta:
        model = MedicalDocument
        fields = '__all__'
        widgets = {            
            'document': TextInput(attrs={'class': 'form-control'}),
            'report': HiddenInput(attrs={'class': 'form-control'}),                                
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  
   
class NatureOfActionForm(ModelForm):    
    
    class Meta:
        model = NatureOfAction
        fields = '__all__'
        widgets = {
            'type_action': TextInput(attrs={'class': 'form-control'}),                                           
            'obs': Textarea(attrs={'class': 'form-control'}),                                           
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  

    def __init__(self, *args, **kwargs):                        
        super().__init__(*args, **kwargs)        
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),                      
            'type_action',  
            'obs',                                                                                         
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_natureofactions_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class TypeItemForm(ModelForm):    
    
    class Meta:
        model = TypeItem
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),            
            'obs': Textarea(attrs={'class': 'form-control'}),
            'medical_specialty': Select(attrs={'class': 'form-control'}),              
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
            'medical_specialty',  
            'obs',                                                                                
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_typeitems_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class TypeItemByNatureOfActionForm(ModelForm):    
    
    class Meta:
        model = TypeItemByNatureOfAction
        fields = '__all__'
        widgets = {
            'type_item': Select(attrs={'class': 'form-control'}),                                           
            'version': TextInput(attrs={'class': 'form-control'}),
            'nature_of_action': Select(attrs={'class': 'form-control'}),
            'question': Textarea(attrs={'class': 'form-control'}),            
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  

    def __init__(self, *args, **kwargs):                       
        self.company = kwargs.get("company","")        
        del(kwargs["company"])         
        super().__init__(*args, **kwargs)        
        self.helper = FormHelper()       
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),
            Hidden('company', self.company),                         
            'type_item',
            'nature_of_action',  
            'version',              
            'question',                                                                                         
            HTML('''               
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	                              
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_typeitembynatureofactions_list' %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

class Item2Form(ModelForm):
    
    class Meta:
        model = Item2
        fields = '__all__'
        widgets = {
            'type_item': HiddenInput(attrs={'class': 'form-control'}),            
            'report': HiddenInput(attrs={'class': 'form-control'}),
            'question': Textarea(attrs={'class': 'form-control'}),
            'answer': Textarea(attrs={'class': 'form-control'}),
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }  