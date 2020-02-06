from django.db import models
from django.contrib.auth.models import User
from PericiasMedicas.patient.models import MaritalStatus
from PericiasMedicas.statescity.models import States2
from PericiasMedicas.company.models import Department

states_choices = []
states = States2.objects.values('uf')
for state in states.values():
    uf = state['uf'].replace("'","").strip(" ")       
    states_choices.append((uf,uf))


class MedicalSpecialty(models.Model):
    name = models.CharField("Nome", max_length=100, blank=False, null= False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="medicalspecialty_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="medicalspecialty_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "MedicalSpecialty"
        verbose_name_plural = "MedicalSpecialties"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class PersonType(models.Model):
    name = models.CharField(("Tipo"), max_length=100, blank=False, null= False)
    user_created = models.ForeignKey(User, related_name="persontype_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="persontype_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    class Meta:
        verbose_name = "PersonType"
        verbose_name_plural = "PersonTypes"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class Person(models.Model):
    sex_choices = [("Masculino","Masculino"), ("Feminino","Feminino")]
    cnh_category_choices = [("A","A"),("AB","AB"),("AC","AC"),("AD","AD"),("AE","AE"),("B","B"),("C","C"),("D","D"),("E","E")]

    name = models.CharField("Nome", max_length=100, blank=False, null= False)
    dt_birthday = models.DateField("Data de Nascimento", max_length=100, blank=False, null=False)
    cpf = models.CharField("CPF", max_length=11, unique=True, blank=False, null=False, help_text="Apenas números")    
    sex = models.CharField("Sexo", max_length = 50, choices=sex_choices, blank=False, null=False)    
    uf_natural = models.CharField("Natural",max_length=100, blank=False, null=False, help_text="Ex: Campo Grande/MS, Porto Alegre/RS, Vitória/ES, Natal/RN")
    maritalstatus = models.ForeignKey(MaritalStatus, verbose_name="Estado Civil", blank=False, null=False,on_delete=models.PROTECT)    
    rg = models.CharField("Nº RG", max_length = 30, blank=True, help_text="Apenas números")
    rg_exped = models.CharField("Orgão Expedidor", max_length = 100,blank=True, help_text="Ex: SSP / DETRAN / FORÇAS ARMADAS / CREA / OAB" )
    rg_uf = models.CharField("RG - UF", choices=states_choices,max_length = 2,blank=True )
    pis_pasep = models.CharField(("PIS/PASEP"), max_length=100, blank=True, help_text = "Apenas Números")
    voter_title_num = models.CharField(("Número do Titulo de Eleitor"), max_length=100, blank=True, help_text = "Apenas Números")
    voter_title_section = models.CharField(("Seção"), max_length=100, blank=True, help_text = "Apenas Números")
    voter_title_zone = models.CharField(("Zona Eleitoral"), max_length=100, blank=True, help_text = "Apenas Números")
    voter_title_uf = models.CharField("UF - Titulo Eleitor", choices=states_choices,max_length = 2, blank=True )
    cnh_num = models.CharField(("Número CNH"), max_length=100, blank=True, help_text = "Apenas Números")
    cnh_uf = models.CharField("CNH - UF", choices=states_choices,max_length = 2, blank=True)
    cnh_validate = models.DateField(("CNH - Validade"), max_length=100, blank=True, null=True)
    cnh_category = models.CharField(("CNH - Categoria"), choices=cnh_category_choices, max_length=100, blank=True)
    address = models.CharField(("Endereço"), max_length=100, blank=True)
    address_num = models.CharField(("Nº"), max_length=100, blank=True, help_text="Apenas Números")
    address_city_uf = models.CharField(("Cidade/UF"), max_length=100, blank=True, help_text="Ex: Campo Grande/MS, Porto Alegre/RS, Vitória/ES, Natal/RN")
    cep = models.CharField(("CEP"), max_length=8, blank=True, help_text = "Apenas Números")        
    email = models.EmailField("Email", max_length=100, blank=True)
    phone = models.CharField("Telefone", max_length=100, blank=True, help_text="Ex:(XX)XXXX-XXXX")
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="person_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="person_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    so = models.CharField(("Sistema Operacional"), max_length=100, blank=True)
    ip = models.CharField(("IP"), max_length=100, blank=True)
    browser = models.CharField(("Navegador"), max_length=100, blank=True)
    avatar = models.ImageField("Foto", upload_to='photo/peoples/', blank=True)
    
    class Meta:
        verbose_name = "Person"
        verbose_name_plural = "People"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class ProfilePersonType(models.Model):
    person = models.ForeignKey(Person, verbose_name=("Pessoa"), on_delete=models.PROTECT)
    person_type = models.ForeignKey(PersonType, verbose_name=("Tipo de Pessoa"), on_delete=models.PROTECT)
    department = models.ForeignKey(Department, verbose_name=("Departamento"), on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="profilepersontype_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="profilepersontype_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "ProfilePersonType"
        verbose_name_plural = "ProfilePersonTypes"
        ordering = ["person"]
    
    def __str__(self):
        return self.person.name
    
class Doctor(models.Model):    
    crm_num = models.CharField("CRM", max_length=30, blank=False, null= False, help_text = "Apenas Números")
    crm_uf = models.CharField("CRM - UF", choices=states_choices,max_length = 2,blank=False )
    course = models.TextField("Titulos", blank=False, null=False, default="")
    medical_specialty = models.ForeignKey(MedicalSpecialty, verbose_name="Especialidade Médica", blank=False, null=False,on_delete=models.PROTECT)
    profile_person_type = models.ForeignKey(ProfilePersonType, verbose_name=("Perito"), on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="doctor_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="doctor_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Doctor"
        verbose_name_plural = "Doctors"
        ordering = ["profile_person_type"]
    
    def __str__(self):
        return "{} - Especialidade: {}".format(self.profile_person_type.person.name, self.medical_specialty)

class DoctorList(models.Model):
    ''' Lista de Médicos. Busca Feita no site do CRM '''
    name = models.CharField("Nome", max_length=100, blank=False, null=False)
    crm = models.CharField(("CRM"), max_length=100, blank=False, null=False)
    situation = models.CharField(("Situação"), max_length=100, blank=True)
    state = models.CharField("UF", choices=states_choices,max_length = 2, blank=False, null=False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    user_created = models.ForeignKey(User, related_name="doctorlist_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="doctorlist_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "DoctorList"
        verbose_name_plural = "DoctorLists"
        ordering = ["name"]
    
    def __str__(self):
        return "{} - {} - {}".format(self.name, self.crm, self.state)

class Cid10(models.Model):
    ''' Lista dos CID-10 existente. Peguei do GitHub 
    link: https://gist.github.com/manuholiveira/9441735
    '''
    category = models.CharField("Categoria", max_length=100, blank=False, null=False)
    description = models.TextField("Descrição", blank=False, null=False)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True, null=True)    
    updated_at = models.DateTimeField('Atualizado em', auto_now=True, null=True)    

    class Meta:
        verbose_name = "Cid10"
        verbose_name_plural = "Cid10"
        ordering = ["category"]
    
    def __str__(self):
        return "{} - {}".format(self.category, self.description)
