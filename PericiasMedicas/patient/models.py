from django.db import models
from django.contrib.auth.models import User
from PericiasMedicas.statescity.models import States2

class Religions(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)    
    abbreviation = models.CharField('Abrev', max_length=100, blank=True)                
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user = models.ForeignKey(User,verbose_name="Usuário", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Religion"
        verbose_name_plural = "Religions"
        ordering = ["name"]
    
    def __str__(self):
        return self.name

class MaritalStatus(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)    
    abbreviation = models.CharField('Abrev', max_length=100, blank=True)                
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.PROTECT)
    
    class Meta:
        verbose_name = "MaritalStatus"
        verbose_name_plural = "MaritalStatus"
        ordering = ["name"]

    def __str__(self):
        return self.name

class Patients(models.Model):
    sex_choices = [("","ESCOLHA"),("Masculino","Masculino"), ("Feminino","Feminino")]
    schooling_choices = [("","ESCOLHA"),("Analfabeto","Analfabeto"),("Ensino Fundamental Incompleto","Ensino Fundamental Incompleto"),("Ensino Fundamental Completo","Ensino Fundamental Completo"), ("Ensino Médio Completo","Ensino Médio Completo"), ("Ensino Médio Incompleto","Ensino Médio Incompleto"), ("Ensino Superior Completo","Ensino Superior Completo"), ("Ensino Superior Incompleto","Ensino Superior Incompleto")]
    type_escort_choices = [("","ESCOLHA"),("Esposo(a)","Esposo(a)"),("Filho(a)","Filho(a)"),("Pai","Pai"),("Mãe","Mãe"),("Tio(a)","Tio(a)"),("Primo(a)","Primo(a)"),("Advogado(a)","Advogado(a)"),("Avô(ó)","Avô(ó)"),("9","Amigo(a)"),("Não Informado","Não Informado")]
    situation_inss_choices = [("","ESCOLHA"),("ATIVO","ATIVO"),("INATIVO","INATIVO")]
    blood_type_choices = [("A","A"),("B","B"),("O","O"),("AB","AB")]
    blood_rh_choices = [("+","+"),("-","-")]
    states_choices = []
    states = States2.objects.values('uf')
    for state in states.values():
        uf = state['uf'].replace("'","").strip(" ")       
        states_choices.append((uf,uf))

    
    name = models.CharField('Nome', max_length=100, blank=False, help_text="Ajuda")    
    dt_birthday = models.DateTimeField("Data de Nascimento", auto_now=False, auto_now_add=False)
    rg = models.CharField("Nº RG", max_length = 30, blank=False, help_text="Apenas números")
    rg_exped = models.CharField("Orgão Expedidor", max_length = 100,blank=False, help_text="Ex: SSP / DETRAN / FORÇAS ARMADAS / CREA / OAB" )
    rg_uf = models.CharField("RG - UF", choices=states_choices,max_length = 2,blank=False )
    cpf = models.CharField("CPF", max_length=11, unique=True, blank=False, help_text="Apenas números")
    name_mother = models.CharField("Nome da Mãe", max_length=100, blank=False)
    name_father = models.CharField("Nome do Pai", max_length=100, blank=True)
    sex = models.CharField("Sexo", max_length = 100, choices=sex_choices, blank=False)
    uf_natural = models.CharField("Naturalidade",max_length=100, blank=False, help_text="Ex: Campo Grande/MS, Porto Alegre/RS, Vitória/ES, Natal/RN")
    origin = models.CharField("Procedência",max_length=100, choices=states_choices, blank=False)
    schooling = models.CharField("Escolaridade", max_length=100, choices=schooling_choices, blank=False)
    maritalstatus = models.ForeignKey(MaritalStatus, verbose_name="Estado Civil",on_delete=models.PROTECT, blank=False)
    religion = models.ForeignKey(Religions, verbose_name="Religião", blank=False, on_delete=models.PROTECT)
    situation_inss = models.CharField("Situação INSS", choices=situation_inss_choices, max_length=100, blank=False)
    scort = models.CharField("Acompanhante", max_length=100, blank=True)    
    scort_type = models.CharField("Parentesco do Acompanhante",choices=type_escort_choices, max_length=100, blank=True)    
    email = models.EmailField("Email", max_length=100, blank=True, null=True)
    phone = models.CharField("Telefone", max_length=30, blank=True, help_text="Ex:(XX)XXXX-XXXX")
    blood_type = models.CharField(("Tipo Sanguíneo"), choices=blood_type_choices, max_length=2, blank=True)
    blood_rh = models.CharField(("FATOR RH"), max_length=2, choices=blood_rh_choices, blank=True)
    address = models.CharField(("Endereço"), max_length=100, blank=True)
    address_num = models.CharField(("Nº"), max_length=100,blank=True, help_text="Apenas números")
    address_city_uf = models.CharField(("Cidade/UF"), max_length=100, blank=True, help_text="Ex: Campo Grande/MS, Porto Alegre/RS, Vitória/ES, Natal/RN")
    cep = models.CharField(("CEP"), max_length=8, blank=True, help_text = "Apenas Números")        
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user = models.ForeignKey(User, verbose_name="Usuário", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Patient"
        verbose_name_plural = "Patients"
    
    def __str__(self):
        return self.name
