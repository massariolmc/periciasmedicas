from django.db import models
from django.contrib.auth.models import User
from PericiasMedicas.patient.models import Patients
from PericiasMedicas.person.models import Person, ProfilePersonType
from PericiasMedicas.company.models import Company, Department
from PericiasMedicas.person.models import MedicalSpecialty
from ckeditor.fields import RichTextField


class ReportStatus(models.Model):
    STATUS_CHOICES = [(0,"Em Produção"),(1, "Finalizado"), (2, "Cancelado"), (3, "Arquivado")]    
    status = models.CharField('Status',max_length=100, blank=False)
    obs = models.TextField(("Observação"), default="", blank= True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="reportstatus_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="reportstatus_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "ReportStatus"
        verbose_name_plural = "ReportStatus"
        ordering = ["status"]

    def __str__(self):
        return self.status


class CidNumber(models.Model):
    codigo = models.CharField("Código", max_length=10,blank=False)
    name = models.CharField("Nome", max_length=100, blank=False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="cidnumbers_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="cidnumbers_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "CidNumber"
        verbose_name_plural = "CidNumbers"
        ordering = ["name"]

    def __str__(self):
        return self.codigo
    

class AuthorityRequesting(models.Model):
    name = models.CharField("Nome", max_length=100, blank=False)
    abbreviation = models.CharField("OBS", max_length=100, blank=True)
    profile_person_type = models.ForeignKey(ProfilePersonType, verbose_name=("Perito"), default="7", on_delete=models.PROTECT)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="authorityrequesting_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="authorityrequesting_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "AuthorityRequesting"
        verbose_name_plural = "AuthorityRequesting"
        ordering = ["name"]

    def __str__(self):
        return self.name

class NatureOfAction(models.Model):
    type_action = models.CharField(("Tipo da Ação"), max_length=100, blank=False, null=False)
    obs = models.TextField(("Observação"), blank=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="natureofaction_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="natureofaction_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)

    class Meta:
        verbose_name = "Nature Of Action"
        verbose_name_plural = "Nature Of Actions"
        ordering = ["type_action"]

    def __str__(self):
        return self.type_action

class ForensicScan(models.Model):
    forensicscan = models.TextField("Circunstância da Perícia", blank=False, null=False)
    goal = models.TextField("Objetivo", blank=False, null=False, default="")    
    profile_person_type = models.ForeignKey(ProfilePersonType, verbose_name=("Perito"), default=1, on_delete=models.PROTECT)    
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), on_delete=models.PROTECT)
    version = models.CharField(("Versão"), max_length=100, default="", blank=False, null=False)
    anamnesis_history = models.TextField("Anamnese: História Pregressa da Doença Atual",blank=True)
    anamnesis_personal_background = models.TextField("Anamnese: Antecedentes Patológicos Pessoais",blank=True)
    anamnesis_family_background = models.TextField("Anamnese: Antecedentes Patológicos Familiares",blank=True)
    anamnesis_general_exam = models.TextField("Anamnese: Exame Físico Geral",blank=True)
    anamnesis_mental_exam = models.TextField("Anamnese: Exame do Estado Mental",blank=True)    
    anamnesis_diagnosis = models.TextField("Anamnese: Diagnóstico",blank=True)
    cid_number = models.CharField(("Informe o CID"), max_length=100, blank=True)    
    discussion = models.TextField("Discussão",blank=True)
    conclusion = models.TextField("Conclusão",blank=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="forensicscans_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="forensicscans_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "ForensicScan"
        verbose_name_plural = "ForensicScans" 

    def __str__(self):
        return self.version     



# A partir daqui tem que criar o report primeiro
class Report(models.Model):
    authority_requesting = models.ForeignKey(AuthorityRequesting, verbose_name=("Autoridade Requisitante"), on_delete=models.PROTECT)    
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), blank=False, null=False, on_delete=models.PROTECT)
    process_number = models.CharField(("Número do Processo"), max_length=50,  unique=True, blank=False, null=False)
    autor = models.ForeignKey(Patients, related_name = "autor_patient_id", verbose_name=("Autor"), blank=False, null=False, on_delete=models.PROTECT)
    proficient = models.ForeignKey(Patients, related_name = "proficient_patient_id", verbose_name=("Periciando"), blank=False, null=False, on_delete=models.PROTECT)
    date_report = models.DateField(("Data da Perícia"), auto_now=False, auto_now_add=False, blank=False)
    profile_person_type = models.ForeignKey(ProfilePersonType, verbose_name=("Perito"), on_delete=models.PROTECT)
    forensic_scan = models.ForeignKey(ForensicScan, blank=True, null=True, verbose_name=("Circunstância da Perícia"), on_delete=models.PROTECT)    
    anamnesis_history = models.TextField("Anamnese: História Pregressa da Doença Atual",blank=True)
    anamnesis_personal_background = models.TextField("Anamnese: Antecedentes Patológicos Pessoais",blank=True)
    anamnesis_family_background = models.TextField("Anamnese: Antecedentes Patológicos Familiares",blank=True)
    anamnesis_general_exam = models.TextField("Anamnese: Exame Físico Geral",blank=True)
    anamnesis_mental_exam = models.TextField("Anamnese: Exame do Estado Mental",blank=True)    
    anamnesis_diagnosis =  models.TextField("Anamnese: Diagnóstico",blank=True)        
    cid_number = models.CharField(("Informe o CID"), max_length=100, blank=True)    
    discussion = models.TextField("Discussão",blank=True)    
    conclusion = models.TextField("Conclusão",blank=True)
    report_status = models.ForeignKey(ReportStatus, verbose_name=("Status"), on_delete=models.PROTECT)
    obs = models.TextField(("Observação"), blank=True)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="report_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="report_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Report"
        verbose_name_plural = "Report"
        ordering = ["id"]

    def __str__(self):        
        patient = Patients.objects.get(pk=self.autor.id)        
        var = "Periciando(a): {} - Processo: {}".format(patient.name,self.process_number)
        return var

class MedicalDocument(models.Model):
    document = models.TextField("Documentos", blank=True)
    report = models.ForeignKey(Report, verbose_name=("Laudo"), on_delete=models.CASCADE)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="medicaldocument_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="medicaldocument_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)


class TypeItem(models.Model):
    name = models.CharField(("Tipo do Quesito"), max_length=100, blank=False, null=False)
    obs = models.TextField(("Obs"), blank=True) 
    #medical_specialty = models.ForeignKey(MedicalSpecialty, verbose_name=("Especialidade"), on_delete=models.PROTECT)       
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="typeitem_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="typeitem_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "TypeItem"
        verbose_name_plural = "TypeItem"
        ordering = ["name"]

    def __str__(self):
        return self.name

class TypeItemByNatureOfAction(models.Model):    
    type_item = models.ForeignKey(TypeItem, verbose_name=("Tipo do Quesito"), on_delete=models.PROTECT)
    version = models.TextField(("Versão"), blank=True)
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), on_delete=models.PROTECT)
    question = models.TextField("Pergunta?", blank=True)    
    company = models.ForeignKey(Company, verbose_name=("Empresa"), default=13,on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="typeitembynatureofaction_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="typeitembynatureofaction_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "TypeItemByNatureOfAction"
        verbose_name_plural = "TypeItemByNatureOfActions"
        ordering = ["version"]

    def __str__(self):
        return self.version


class Item2(models.Model):
    #type_item_by_nature_of_action = models.ForeignKey(TypeItemByNatureOfAction, verbose_name=("Tipo do Quesito"), on_delete=models.PROTECT)
    type_item = models.ForeignKey(TypeItem ,verbose_name=("Tipo do Quesito"), on_delete=models.CASCADE)
    report = models.ForeignKey(Report, verbose_name=("Laudo"), on_delete=models.CASCADE)
    question = models.TextField("Pergunta?", blank=True) 
    answer = models.TextField("Resposta", blank=True)
    answer_status = models.BooleanField("Finalizar", blank=True)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="item2_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="item2_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Item2"
        verbose_name_plural = "Items2"
        ordering = ["report"]

    def __str__(self):
        return self.report.process_number
