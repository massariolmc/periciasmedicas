from django.db import models
from django.contrib.auth.models import User
from PericiasMedicas.statescity.models import States2

states_choices = []
states = States2.objects.values('uf')
for state in states.values():
    uf = state['uf'].replace("'","").strip(" ")       
    states_choices.append((uf,uf))

class CompanyType(models.Model):
    name = models.CharField(("Nome"), max_length=100, blank=False, null= False)
    abbreviation = models.CharField(("Abreviação"), max_length=100, blank=True, null= True)
    user_created = models.ForeignKey(User, related_name="company_types_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="company_ypes_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "CompanyType"
        verbose_name_plural = "CompanyTypes"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class CompanyTaxRegime(models.Model):
    name = models.CharField(("Nome"), max_length=100, blank=False, null= False)
    abbreviation = models.CharField(("Abreviação"), max_length=100, blank=True, null= True)
    user_created = models.ForeignKey(User, related_name="company_tax_regime_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="company_tax_regime_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "CompanyTaxRegime"
        verbose_name_plural = "CompanyTaxRegimes"
        ordering = ["name"]
    
    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(("Nome"), max_length=100, blank=False, null= False)
    cnpj = models.CharField(("CNPJ"), max_length=14, unique = True, blank=True)
    state_registration = models.CharField(("Inscrição Estadual"), default="",max_length=100, blank=True)    
    abbreviation = models.CharField(("Abreviação"), max_length=100, blank=True)
    tax_regime = models.ForeignKey(CompanyTaxRegime, default="",verbose_name ="Regime Tributário", blank=True, on_delete=models.PROTECT)    
    company_type = models.ForeignKey(CompanyType, default="", verbose_name="Tipo de Empresa", blank=True, on_delete=models.PROTECT)
    address = models.CharField(("Endereço"), max_length=100, blank=False, null= False)
    address_num = models.CharField(("Número"), max_length=100, blank=False, null= False)
    address_burgh = models.CharField(("Bairro"), max_length=100, blank=False, null= False)
    state_city = models.CharField(("Cidade/Estado"), max_length=100, blank=False, null= False)
    zip_code = models.CharField(("CEP"), max_length=8, blank=True)
    user_created = models.ForeignKey(User, related_name="company_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="company_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(("Nome"), max_length=100, blank=False, null= False)
    abbreviation = models.CharField(("Sigla"), max_length=100, blank=True)
    company = models.ForeignKey(Company, verbose_name=("Empresa"), on_delete=models.PROTECT, blank=False, null= False)
    user_created = models.ForeignKey(User, related_name="department_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="department_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
    class Meta:
        verbose_name = "Department"
        verbose_name_plural = "Departments"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

