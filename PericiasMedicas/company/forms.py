from django.forms import ModelForm, TextInput, DateInput, Select, SelectDateWidget, HiddenInput, DateTimeInput, EmailInput
from .models import Company, Department
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Button, ButtonHolder, HTML, Hidden
from django.core.exceptions import ValidationError

class CompanyForm(ModelForm):

    class Meta:
        model = Company
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),
            'cnpj': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'state_registration': TextInput(attrs={'class': 'form-control cpf','onkeypress':'return somenteNumeros(event)'}),
            'abbreviation': TextInput(attrs={'class': 'form-control'}),
            'tax_regime': Select(attrs={'class': 'form-control'}),
            'company_type': Select(attrs={'class': 'form-control'}),
            'address': TextInput(attrs={'class': 'form-control'}),
            'address_num': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),
            'address_burgh': TextInput(attrs={'class': 'form-control'}),
            'state_city': TextInput(attrs={'class': 'cidade_estado'}),
            'zip_code': TextInput(attrs={'class': 'form-control','onkeypress':'return somenteNumeros(event)'}),            
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
        error_messages = {
            'name': {
                'blank': ("Não pode ser em branco."),
            },
        }
    
    #VALIDAÇÃO
    def clean_name(self):        
        name = self.cleaned_data['name']
        if self.instance.id:
            n = Company.objects.filter(name__iexact=name).exclude(id=self.instance.id).exists()#Verifica se o nome já existe            
        else:
            n = Company.objects.filter(name__iexact=name).exists()#Verifica se o nome já existe                
        if n:            
            raise ValidationError("Nome já existente. Informe outro.")
        return name
        
    #VALIDAÇÃO
    def clean_cnpj(self):
        cnpj = self.cleaned_data['cnpj']
        tam = len(cnpj)        
        if tam > 0 and tam < 14:
            raise ValidationError("O CNPJ deve ter 14 digitos.")
        return cnpj

    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),            
            'name',
            Row(
                Column('cnpj', css_class='form-group col-md-4 mb-0'),
                Column('state_registration', css_class='form-group col-md-4 mb-0'),
                Column('abbreviation', css_class='form-group col-md-4 mb-0'),                
                css_class='form-row'
            ),
            'tax_regime',
            'company_type',
            Row(
                Column('address', css_class='form-group col-md-4 mb-0'),
                Column('address_num', css_class='form-group col-md-1 mb-0'),
                Column('address_burgh', css_class='form-group col-md-2 mb-0'),
                Column('state_city', css_class='form-group col-md-3 mb-0'),
                Column('zip_code', css_class='form-group col-md-2 mb-0'),
                css_class='form-row'
            ),
            HTML('''
                 <div class="row">    
                    <div class="col-sm-6">
                        <span class="float-left">
                            <button type="submit" class="btn btn-primary">Salvar</button>  	  
                            <button type="reset" class="btn btn-secondary">Limpar formulário</button>
                        </span>
                    </div>
                    <div class="col-sm-6">
                        <span class="float-right">
                            <a href="{% url 'url_companies_list'%}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),       
            
            
        )


class DepartmentForm(ModelForm):

    class Meta:
        model = Department
        fields = '__all__'
        widgets = {
            'name': TextInput(attrs={'class': 'form-control'}),                        
            'abbreviation': TextInput(attrs={'class': 'form-control'}),            
            'company': HiddenInput(attrs={'class': 'form-control'}),                       
            'user_created': HiddenInput(attrs={'class': 'form-control'}),
            'user_updated': HiddenInput(attrs={'class': 'form-control'}),            
        }
        error_messages = {
            'name': {
                'blank': ("Não pode ser em branco."),
            },
        }
    
    # Django Validations  - customizado
    def clean(self):
        print("Entrei no clean name", self.cleaned_data)
        name = self.cleaned_data['name']           
        company_id = self.cleaned_data['company']                
        if self.instance.id:
            n = Department.objects.filter(name__iexact=name, company_id=self.instance.company_id).exclude(id=self.instance.id).exists()#Verifica se o nome já existe        
            
        else:            
            n = Department.objects.filter(name__iexact=name, company_id=company_id).exists()#Verifica se o nome já existe        
            
        if n:            
            raise ValidationError("Departamento já existente. Informe outro nome.")
        
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            Hidden('user_created', '{{ user.id }}'),
            Hidden('user_updated', '{{ user.id }}'),            
            Hidden('company','{{ company_id }}'),
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
                            <a href="{% url 'url_show_departments_company' company_id %}" class="btn btn-warning">Voltar</a>
                        </span>  
                    </div>
                </div>'''
            ),         
        )

