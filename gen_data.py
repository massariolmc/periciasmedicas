import os
import django
import string
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "PericiasMedicas.settings")
django.setup()
from PericiasMedicas.statescity.models import Countries, States2, Cities
from PericiasMedicas.person.models import Person, DoctorList, MedicalSpecialty, Doctor
from PericiasMedicas.patient.models import MaritalStatus
from PericiasMedicas.company.models import Company, CompanyTaxRegime, CompanyType, Department
from PericiasMedicas.report.models import DiscussionConclusion,TypeItemByNatureOfAction, TypeItem, NatureOfAction
from django.contrib.auth.models import User
from datetime import datetime

#Fiz para popular as tabelas País, Estado e Cidade
class CountriesClass:

    def inserir_pais():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/estado.txt','r')
        for read in arq.readlines():            
            aux = read[1:-3].split(",")
            #aux = read.split("\t")
            print(aux[1])
            data = dict(
                # name    =   aux[1],
                # name_pt =   aux[2],
                # acronym =   aux[3],
                # bacen   =   aux[4],
                name    = aux[1],                
                uf      = aux[2],
                ibge    = aux[3],
                #lat_lon = aux[4],
                country =   aux[4],
                ddd = aux[5],
            )
            obj = States2(**data)
            #obj = Cities(**data)
            aux2.append(obj)
        States2.objects.bulk_create(aux2)

#CountriesClass.inserir_pais()

class PersonPopulate():
    def inserir_person():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/Person.txt','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)
            data = dict(
                name = aux[0],
                dt_birthday = datetime.strptime(aux[1], '%d-%m-%Y %H:%M:%S'),
                cpf = aux[2],
                sex = aux[3],
                uf_natural = aux[4],
                maritalstatus = MaritalStatus.objects.get(pk=aux[5]),
                rg = aux[6],
                rg_exped = aux[7],
                rg_uf = aux[8],
                pis_pasep = aux[9],
                voter_title_num = aux[10],
                voter_title_section = aux[11],
                voter_title_zone = aux[12],
                voter_title_uf = aux[13],
                cnh_num = aux[14],
                cnh_uf = aux[15],
                cnh_validate = datetime.strptime(aux[16], '%d-%m-%Y'),
                cnh_category = aux[17],
                address = aux[18],
                address_num = aux[19],
                address_city_uf = aux[20],
                cep = aux[21],
                email = aux[22],
                phone = aux[23] ,         
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            obj = Person(**data)            
            aux2.append(obj)
        Person.objects.bulk_create(aux2)

#PersonPopulate.inserir_person()

class CompanyPopulate():

    def inserir_company():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/Company.txt','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)
            data = dict(
                name = aux[0],
                cnpj = aux[1],
                state_registration = aux[2],
                abbreviation = aux[3],
                tax_regime = CompanyTaxRegime.objects.get(pk=aux[4]),
                company_type = CompanyType.objects.get(pk=aux[5]),
                address = aux[6],
                address_num = aux[7],
                address_burgh = aux[8],
                state_city = aux[9],
                zip_code = aux[10],                
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            obj = Company(**data)            
            aux2.append(obj)
        Company.objects.bulk_create(aux2)
#CompanyPopulate.inserir_company()        

class DepartmentPopulate():

    def inserir_department():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/Department.txt','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)
            data = dict(
                name = aux[0],                
                abbreviation = aux[1],
                company = Company.objects.get(pk=aux[2]),                               
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            obj = Department(**data)            
            aux2.append(obj)
        Department.objects.bulk_create(aux2)
#DepartmentPopulate.inserir_department() 

class DoctorListPopulate():
    ''' Class para inserir a lista de médicos psquiatras do MS '''
    def inserir_doctorlist():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/Psiquiatras_MS.txt','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)#Lista a linha que vai ser inserida            
            data = dict(
                name = aux[0],                
                situation = aux[1],
                crm = aux[2],
                state = aux[3].strip(),# Tira o espaço em branco na última linha                               
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            obj = DoctorList(**data)            
            aux2.append(obj)
        DoctorList.objects.bulk_create(aux2)
#DoctorListPopulate.inserir_doctorlist() 

class MedicalSpecialtyPopulate():
    ''' Inserir Especialidades Médicas '''
    def inserir_medicalspecialtylist():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/Lista_Especialidades_Medicas.txt','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            #aux = read.split(";")
            print(read)#Lista a linha que vai ser inserida                        
            data = dict(
                name = read.strip(),                                                               
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            obj = MedicalSpecialty(**data)            
            aux2.append(obj)
        MedicalSpecialty.objects.bulk_create(aux2)
#MedicalSpecialtyPopulate.inserir_medicalspecialtylist() 

class DiscussionConclusionPopulate():
    ''' Inserir Discussion e Conclusion '''
    def inserir_discussion_conclusion():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/JACKSON_DISCUSSAO.csv','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)#Lista a linha que vai ser inserida
            print(aux)#Lista a linha que vai ser inserida                        
            data = dict(
                cid_number = aux[0].strip(),
                doctor = Doctor.objects.get(pk=int(aux[1])),
                discussion = aux[2].strip(),
                conclusion = aux[3].strip(),    
                version = aux[4].strip(),                                                               
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            print("Valor do data",data)
            obj = DiscussionConclusion(**data)            
            aux2.append(obj)
        DiscussionConclusion.objects.bulk_create(aux2)
#DiscussionConclusionPopulate.inserir_discussion_conclusion() 

class TypeItemByNatureOfActionPopulate():
    ''' Inserir modelos dos quesitos '''
    def inserir_modelos_quesitos():
        aux = []
        aux2 = []
        arq = open('/home/massariol/Documentos/Apps/DJANGO/COMPILADO_QUESITOS_JACKSON.csv','r')
        for read in arq.readlines():            
            #aux = read[1:-3].split(",")
            aux = read.split(";")
            print(read)#Lista a linha que vai ser inserida
            print(aux)#Lista a linha que vai ser inserida                        
            data = dict(
                type_item = TypeItem.objects.get(pk=int(aux[0])),
                nature_of_action = NatureOfAction.objects.get(pk=int(aux[1])),
                doctor = Doctor.objects.get(pk=int(aux[2])),
                cid_number = aux[3].strip(),    
                question = aux[4].strip(),   
                answer = aux[5].strip(),   
                version = aux[6].strip(),                                                               
                user_created = User.objects.get(pk=1), 
                user_updated = User.objects.get(pk=1),
            )
            print("Valor do data",data)
            obj = TypeItemByNatureOfAction(**data)            
            aux2.append(obj)
        TypeItemByNatureOfAction.objects.bulk_create(aux2)
TypeItemByNatureOfActionPopulate.inserir_modelos_quesitos() 
