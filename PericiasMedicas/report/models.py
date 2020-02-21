from django.db import models
from django.contrib.auth.models import User
from PericiasMedicas.patient.models import Patients
from PericiasMedicas.person.models import Person, ProfilePersonType,Doctor
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
  
class AuthorityRequesting(models.Model):
    name = models.CharField("Forma de tratamento da Autoridade", max_length=100, blank=False)
    abbreviation = models.CharField("OBS", max_length=100, blank=True)
    #profile_person_type = models.ForeignKey(ProfilePersonType, verbose_name=("Perito"), default="7", on_delete=models.PROTECT)    
    doctor = models.ForeignKey(Doctor, verbose_name=("Perito"), on_delete=models.PROTECT)    
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

class LocationObjective(models.Model):
    forensic_scan = RichTextField("Circunstância da Perícia", blank=False, null=False, default="")
    goal = RichTextField("Objetivo", blank=False, null=False)    
    doctor = models.ForeignKey(Doctor, verbose_name=("Perito"), on_delete=models.PROTECT)    
    version = models.CharField("Versão", max_length=100, blank=False, null=False, default="")
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="locationobjective_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="locationobjective_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "LocationObjective"
        verbose_name_plural = "LocationObjectives" 

    def __str__(self):
        return "Versão: {} - Perito: {}".format(self.version,self.doctor)

class ForensicScan(models.Model):    
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), on_delete=models.PROTECT)
    version = models.CharField(("Versão"), max_length=100, blank=False, null=False)    
    doctor = models.ForeignKey(Doctor,verbose_name=("Perito"), on_delete=models.PROTECT)
    anamnesis_family = RichTextField("Anamnese: História Familiar",blank=True)
    anamnesis_professional = RichTextField("Anamnese: História Profissional",blank=True)
    anamnesis_conditions = RichTextField("Anamnese: Condições de Parto e Desenvolvimento Neuropsicomotor",blank=True)
    anamnesis_history = RichTextField("Anamnese: História Pregressa da Doença Atual",blank=True)
    anamnesis_personal_background = RichTextField("Anamnese: Antecedentes Patológicos Pessoais",blank=True)
    anamnesis_family_background = RichTextField("Anamnese: Antecedentes Patológicos Familiares",blank=True)
    anamnesis_general_exam = RichTextField("Anamnese: Exame Físico Geral",blank=True)
    anamnesis_mental_exam = RichTextField("Anamnese: Exame do Estado Mental",blank=True)        
    cid_number = models.CharField(("Informe o CID"), max_length=100, blank=True)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="forensicscans_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="forensicscans_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "ForensicScan"
        verbose_name_plural = "ForensicScans" 

    def __str__(self):
        return "Perito: {} - Versão: {}".format(self.doctor,self.version)

class DiscussionConclusion(models.Model):   

    cid_number = models.CharField(("Informe o CID"), max_length=7, blank=False, null=False)    
    doctor = models.ForeignKey(Doctor, default=7,verbose_name=("Perito"), on_delete=models.PROTECT)    
    discussion = RichTextField("Discussão",blank=True)
    conclusion = RichTextField("Conclusão",blank=True)    
    version = models.CharField("Versão", max_length=100, blank=False, null=False)
    #version = models.TextField("Versão", blank=False, null=False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="discussionconclusion_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="discussionconclusion_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "DiscussionConclusion"
        verbose_name_plural = "DiscussionConclusions" 

    def __str__(self):
        return "Cid: {}".format(self.cid_number)

# A partir daqui tem que criar o report primeiro
class Report(models.Model):
    INABILITY_PROFESSIONAL_CHOICES = [("","ESCOLHA"),("uniprofissional","UNIPROFSSIONAL"),("multiprofissional", "MULTIPROFISSIONAL"), ("omniprofissional", "OMNIPROFISSIONAL")]    
    INABILITY_TEMPORAL_CHOICES = [("","ESCOLHA"),("temporária","TEMPORÁRIA"),("permanente", "PERMANENTE")]    

    authority_requesting = models.ForeignKey(AuthorityRequesting, verbose_name=("Autoridade Requisitante"), on_delete=models.PROTECT)    
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), blank=False, null=False, on_delete=models.PROTECT)
    process_number = models.CharField(("Número do Processo"), max_length=50,  unique=True, blank=False, null=False)
    autor = models.ForeignKey(Patients, related_name = "autor_patient_id", verbose_name=("Autor"), blank=False, null=False, on_delete=models.PROTECT)
    proficient = models.ForeignKey(Patients, related_name = "proficient_patient_id", verbose_name=("Periciando"), blank=False, null=False, on_delete=models.PROTECT)
    date_report = models.DateField(("Data da Perícia"), auto_now=False, auto_now_add=False, blank=False)    
    doctor = models.ForeignKey(Doctor, default=7,verbose_name=("Perito"), on_delete=models.PROTECT)
    location_objective = models.ForeignKey(LocationObjective, blank=True, null=True, verbose_name=("Local e Objetivo"), on_delete=models.PROTECT)
    forensic_scan = models.ForeignKey(ForensicScan, blank=True, null=True, verbose_name=("Qual modelo de anamnese?"), on_delete=models.PROTECT)    
    anamnesis_family = RichTextField("Anamnese: História Familiar",blank=True)
    anamnesis_professional = RichTextField("Anamnese: História Profissional",blank=True)
    anamnesis_conditions = RichTextField("Anamnese: Condições de Parto e Desenvolvimento Neuropsicomotor",blank=True)
    anamnesis_history = RichTextField("Anamnese: História Pregressa da Doença Atual",blank=True)
    anamnesis_personal_background = RichTextField("Anamnese: Antecedentes Patológicos Pessoais",blank=True)
    anamnesis_family_background = RichTextField("Anamnese: Antecedentes Patológicos Familiares",blank=True)
    anamnesis_general_exam = RichTextField("Anamnese: Exame Físico Geral",blank=True)
    anamnesis_mental_exam = RichTextField("Anamnese: Exame do Estado Mental",blank=True)        
    discussion = RichTextField("Discussão",blank=True)    
    conclusion = RichTextField("Conclusão",blank=True)
    inability_professional = models.CharField("Incapacidade Profissional", choices=INABILITY_PROFESSIONAL_CHOICES, max_length=100, blank=True, null=True)
    inability_temporal = models.CharField("Duração da Incapacidade", max_length=100, choices=INABILITY_TEMPORAL_CHOICES, blank=True, null=True)
    report_status = models.ForeignKey(ReportStatus, verbose_name=("Status"), on_delete=models.PROTECT)
    obs = models.TextField(("Observação"), blank=True)
    impress = RichTextField("Impressão",blank=True)
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

class CidNumber(models.Model):
    category = models.CharField("Categoria", max_length=7,blank=False, null=False)    
    description = models.TextField("Descrição", blank=False, null=False)
    report = models.ForeignKey(Report, verbose_name=("Laudo"), on_delete=models.CASCADE, blank=False, null=False)
    type_cid = models.BooleanField("Informe o CID primário", blank=False, default=False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="cidnumbers_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="cidnumbers_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "CidNumber"
        verbose_name_plural = "CidNumbers"
        ordering = ["-type_cid","category"]

    def __str__(self):
        return "Categoria: {} / Descrição: {}".format(self.category, self.description)

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

#Modelos de Quesitos por natureza de ação
class TypeItemByNatureOfAction(models.Model):    
    type_item = models.ForeignKey(TypeItem, verbose_name=("Tipo do Quesito"), on_delete=models.PROTECT)
    version = models.TextField(("Versão"), blank=True)
    doctor = models.ForeignKey(Doctor,verbose_name=("Perito"), on_delete=models.PROTECT)    
    nature_of_action = models.ForeignKey(NatureOfAction, verbose_name=("Natureza da Ação"), on_delete=models.PROTECT)
    question = RichTextField("Pergunta?", blank=True)
    answer = RichTextField("Resposta", blank=True)       
    cid_number = models.CharField("CID-10", max_length=100, blank=False, null=False)
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="typeitembynatureofaction_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="typeitembynatureofaction_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "TypeItemByNatureOfAction"
        verbose_name_plural = "TypeItemByNatureOfActions"
        ordering = ["version","-id"]

    def __str__(self):
        return self.version
#Quesitos do Laudos
class Item2(models.Model):    
    type_item = models.ForeignKey(TypeItem ,verbose_name=("Tipo do Quesito"), on_delete=models.CASCADE)
    report = models.ForeignKey(Report, verbose_name=("Laudo"), on_delete=models.CASCADE)
    question = RichTextField("Pergunta?", blank=True) 
    answer = RichTextField("Resposta", blank=True)
    answer_status = models.BooleanField("Finalizar", blank=True)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True) 
    user_created = models.ForeignKey(User, related_name="item2_user_created_id", verbose_name="Criado por", on_delete=models.PROTECT)
    user_updated = models.ForeignKey(User, related_name="item2_user_updated_id", verbose_name="Atualizado por", on_delete=models.PROTECT)
    class Meta:
        verbose_name = "Item2"
        verbose_name_plural = "Items2"
        #ordering = ["report"]

    def __str__(self):
        return self.report.process_number
