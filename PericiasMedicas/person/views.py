from django.shortcuts import render,get_object_or_404, get_list_or_404, redirect
from django.http import JsonResponse, HttpResponse
from .forms import PersonForm, PersonTypeForm, ProfilePersonTypeForm, MedicalSpecialtyForm, DoctorForm, DoctorListForm
from .models import Person, PersonType, ProfilePersonType, MedicalSpecialty, Doctor, DoctorList, Cid10
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PericiasMedicas.statescity.models import States2, Cities
from PericiasMedicas.company.models import Department, Company
from django.db.models import Q


######  PERSON   #######################################
@login_required
def person_create(request):
    template_name = 'person/form.html'
    data = {}
    ip = request.META['REMOTE_ADDR']
    so = request.META['HTTP_USER_AGENT'].split() # Essa linha mostra o sistema operacional e navegador do usuário   
    if request.method == 'POST':        
        form = PersonForm(request.POST)
        if form.is_valid():
            person = form.save(commit=False)            
            person.ip = ip
            person.so = so[2] + so[3] + so[4]
            person.browser = so[-1]         
            person.save()                    
            return redirect('url_people_list')
        else:
            print("algo não está valido.")
    else:
        form = PersonForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def people_list(request):
    template_name = "person/list.html"    
    people = Person.objects.all()    
    context = {
        'people': people,              
    }
    return render(request,template_name,context)

@login_required
def person_detail(request, pk=None, *args, **kwargs):
    template_name = "person/detail.html"
    person = get_object_or_404(Person,pk=pk)
    context = {
        'person': person
    }
    return render(request, template_name, context)

@login_required
def person_edit(request, pk):    
    template_name='person/form.html'
    data = {}
    ip = request.META['REMOTE_ADDR']
    so = request.META['HTTP_USER_AGENT'].split() # Essa linha mostra o sistema operacional e navegador do usuário   
    person = get_object_or_404(Person, pk=pk)        
    user_created = person.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = PersonForm(request.POST or None, instance=person)
    if form.is_valid():        
        person = form.save(commit=False)
        person.user_created = user_created
        person.ip = ip
        person.so = so[2] + so[3] + so[4]
        person.browser = so[-1]         
        person.save()
        return redirect('url_person_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def person_delete(request,pk):
    person = get_object_or_404(Person, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        person.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_people_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_people_list')


#####FIM DO PERSON########################################

##### PERSON TYPE #######################################

@login_required
def persontype_create(request):
    template_name = 'persontype/form.html'
    data = {}
    data['title'] = "Cadastro de Tipos de Pessoas"        
    if request.method == 'POST':        
        form = PersonTypeForm(request.POST)
        if form.is_valid():
            form.save()                        
            return redirect('url_persontypes_list')
        else:
            print("algo não está valido.")
    else:
        form = PersonTypeForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def persontypes_list(request):
    template_name = "persontype/list.html"
    persontypes = PersonType.objects.all()    
    context = {
        'persontypes': persontypes,
        'title': "Tipos cadastrados"      
    }
    return render(request,template_name,context)

@login_required
def persontype_detail(request, pk=None, *args, **kwargs):
    template_name = "persontype/detail.html"
    persontype = get_object_or_404(PersonType,pk=pk)
    context = {
        'persontype': persontype
    }
    return render(request, template_name, context)

@login_required
def persontype_edit(request, pk):    
    template_name='persontype/form.html'
    data = {} 
    persontype = get_object_or_404(PersonType, pk=pk)        
    user_created = persontype.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = PersonTypeForm(request.POST or None, instance=persontype)
    if form.is_valid():        
        persontype = form.save(commit=False)
        persontype.user_created = user_created               
        persontype.save()
        return redirect('url_persontype_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def persontype_delete(request,pk):
    persontype = get_object_or_404(PersonType, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        persontype.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_persontypes_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_persontypes_list')


###### FIM PERSON TYPES###################################

######## PROFILE PERSON TYPE #############################

@login_required
def profilepersontype_save(request):   
    print("Request do SAVE: ", request.method)       
    if request.method == 'POST':
        print("Entrei no post do SAVE") 
        print("Valores da request total", request.POST)       
        print("Valores da request: {}, {}, {}".format(request.POST['person'], request.POST['person_type'], request.POST['department']))
        form = ProfilePersonTypeForm(request.POST)
        print("Passei do form")
        data = {}               
        if form.is_valid():
            person = form.save(commit=False)
            department = person.department_id
            print("Valor do department id", department)
            person.save()                        
            return redirect('url_profilepersontypes_list', pk=department)
        else:
            print("algo não está valido.")
            form = ProfilePersonTypeForm()            
    else:
        form = ProfilePersonTypeForm()             
    
    data['form'] = form
    return render(request,'profilepersontype/form.html',data)

def profilepersontype_create(request,pk):
    template_name = 'profilepersontype/form.html'
    department = Department.objects.get(pk=pk)
    company = Company.objects.get(pk=department.company_id)
    title1 = "Empresa: "
    title2 = "Departamento: "
    title3 = "Cadastro de Funcionário"
    data = {
        'department_name': department.name,  
        'department_id': department.id,       
        'title1': title1,
        'title2': title2,
        'title3': title3,
        'company_name': company.name
    }           
    if request.method == 'GET':        
        print("Entrou o GET")
        form = ProfilePersonTypeForm()
        data['form'] = form
        return render(request,template_name,data)
        
    else:
        print("Entrou no ElSE")
        form = ProfilePersonTypeForm(request.POST or None)
        print("Passei do form")
        data = {}               
        if form.is_valid():
            person = form.save(commit=False)
            department = person.department_id
            print("Valor do department id", department)
            person.save()                        
            return redirect('url_profilepersontypes_list', pk=department)
        else:
            print("algo não está valido.")
            form = ProfilePersonTypeForm()
    data['form'] = form
    return render(request,'profilepersontype/form.html',data)    
    

@login_required
def profilepersontypes_list(request,pk):
    template_name = "profilepersontype/list.html"
    department = Department.objects.get(pk=pk)
    company = Company.objects.get(pk=department.company_id)
    title1 = "Empresa: "
    title2 = "Funcionários do Departamento: "
    context = {
        'department_name': department.name,
        'department_id': department.id,
        'title1': title1,
        'title2': title2,
        'company_name': company.name
    }
    if request.method == 'GET':               
        profilepersontypes = ProfilePersonType.objects.filter(department_id=pk) 
        if profilepersontypes:                          
            context['profilepersontypes'] = profilepersontypes      
            return render(request,template_name,context)
        else:                 
            messages.warning(request,'Não existem funcionários neste departamento.')
            return render(request,template_name,context)
    else:        
        messages.warning(request, 'Contacte o Administrador.')
        return redirect('url_show_departments_company', department.id)

@login_required
def profilepersontype_detail(request, pk=None, *args, **kwargs):
    template_name = "profilepersontype/detail.html"
    profilepersontype = get_object_or_404(ProfilePersonType,pk=pk)
    context = {
        'profilepersontype': profilepersontype
    }
    return render(request, template_name, context)

@login_required
def profilepersontype_edit(request, pk):    
    template_name='profilepersontype/form.html'
    profilepersontype = get_object_or_404(ProfilePersonType, pk=pk)       
    department = Department.objects.get(pk=profilepersontype.department_id)
    company = Company.objects.get(pk=department.company_id)        
    title1 = "Empresa: "
    title2 = "Departamento: "
    title3 = "Cadastro de Funcionário"
    data = {
        'department_name': department.name,  
        'department_id': department.id,               
        'title1': title1,
        'title2': title2,
        'title3': title3,
        'company_name': company.name
    }                
    user_created = profilepersontype.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    profilepersontype_id = profilepersontype.id
    form = ProfilePersonTypeForm(request.POST or None, instance=profilepersontype, person_name=profilepersontype.person.name, person_id=profilepersontype.person_id)
    if form.is_valid():        
        profilepersontype = form.save(commit=False)
        profilepersontype.user_created = user_created               
        profilepersontype.save()
        return redirect('url_profilepersontype_detail',pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def profilepersontype_delete(request,pk):
    profilepersontype = get_object_or_404(ProfilePersonType, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        profilepersontype.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_profilepersontypes_list', profilepersontype.department_id)
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_profilepersontypes_list', profilepersontype.department_id)


######### FIM PROFILE PERSON TYPE #######################

######### DOCTOR ################
@login_required
def doctor_create(request):
    template_name = 'doctor/form.html'
    data = {}
    data['title'] = "Cadastro dos Peritos"        
    if request.method == 'POST':        
        form = DoctorForm(request.POST)
        if form.is_valid():
            form.save()                        
            return redirect('url_doctors_list')
        else:
            print("algo não está valido.")
    else:
        form = DoctorForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def doctors_list(request):
    template_name = "doctor/list.html"
    title = "Especialidades Médicas"
    doctors = Doctor.objects.all()    
    context = {
        'doctors': doctors,
        'title': title      
    }
    return render(request,template_name,context)

@login_required
def doctor_detail(request, pk=None, *args, **kwargs):
    template_name = "doctor/detail.html"
    doctor = get_object_or_404(Doctor,pk=pk)
    context = {
        'doctor': doctor
    }
    return render(request, template_name, context)

@login_required
def doctor_edit(request, pk):    
    template_name='doctor/form.html'
    data = {} 
    doctor = get_object_or_404(Doctor, pk=pk)        
    user_created = doctor.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = DoctorForm(request.POST or None, instance=doctor)
    if form.is_valid():        
        doctor = form.save(commit=False)
        doctor.user_created = user_created               
        doctor.save()
        return redirect('url_doctor_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def doctor_delete(request,pk):
    doctor = get_object_or_404(Doctor, pk=pk)    
    if request.method == 'GET':        
        doctor.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_doctors_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_doctors_list')


######### FIM DOCTOR ############

######### MedicalSpecialty #####
@login_required
def medicalspecialty_create(request):
    template_name = 'medicalspecialty/form.html'
    data = {}
    data['title'] = "Cadastro das Especialidades Médicas"        
    if request.method == 'POST':        
        form = MedicalSpecialtyForm(request.POST)
        if form.is_valid():
            form.save()                        
            return redirect('url_medicalspecialties_list')
        else:
            print("algo não está valido.")
    else:
        form = MedicalSpecialtyForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def medicalspecialties_list(request):
    template_name = "medicalspecialty/list.html"
    title = "Especialidades Médicas"
    medicalspecialties = MedicalSpecialty.objects.all()    
    context = {
        'medicalspecialties': medicalspecialties,
        'title': title      
    }
    return render(request,template_name,context)

@login_required
def medicalspecialty_detail(request, pk=None, *args, **kwargs):
    template_name = "medicalspecialty/detail.html"
    medicalspecialty = get_object_or_404(MedicalSpecialty,pk=pk)
    context = {
        'medicalspecialty': medicalspecialty
    }
    return render(request, template_name, context)

@login_required
def medicalspecialty_edit(request, pk):    
    template_name='medicalspecialty/form.html'
    data = {} 
    medicalspecialty = get_object_or_404(MedicalSpecialty, pk=pk)        
    user_created = medicalspecialty.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = MedicalSpecialtyForm(request.POST or None, instance=medicalspecialty)
    if form.is_valid():        
        medicalspecialty = form.save(commit=False)
        medicalspecialty.user_created = user_created               
        medicalspecialty.save()
        return redirect('url_medicalspecialty_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def medicalspecialty_delete(request,pk):
    medicalspecialty = get_object_or_404(MedicalSpecialty, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        medicalspecialty.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_medicalspecialties_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_medicalspecialties_list')

######## FIM MedicalSpecialty ###

############### DOCSTOR LIST ####

@login_required
def doctorlist_create(request):
    template_name = 'doctorlist/form.html'
    data = {}
    data['title'] = "Cadastro dos Médicos Psiquiatras do MS"        
    if request.method == 'POST':        
        form = DoctorListForm(request.POST)
        if form.is_valid():
            form.save()                        
            return redirect('url_doctorlists_list')
        else:
            print("algo não está valido.")
    else:
        form = DoctorListForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def doctorlists_list(request):
    template_name = "doctorlist/list.html"
    title = "Lista dos Médicos Psiquiatras do MS"
    doctorlists = DoctorList.objects.all()    
    context = {
        'doctorlists': doctorlists,
        'title': title      
    }
    return render(request,template_name,context)

@login_required
def doctorlist_detail(request, pk=None, *args, **kwargs):
    template_name = "doctorlist/detail.html"
    doctorlist = get_object_or_404(DoctorList,pk=pk)
    context = {
        'doctorlist': doctorlist
    }
    return render(request, template_name, context)

@login_required
def doctorlist_edit(request, pk):    
    template_name='doctorlist/form.html'
    data = {} 
    doctorlist = get_object_or_404(DoctorList, pk=pk)        
    user_created = doctorlist.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = DoctorListForm(request.POST or None, instance=doctorlist)
    if form.is_valid():        
        doctorlist = form.save(commit=False)
        doctorlist.user_created = user_created               
        doctorlist.save()
        return redirect('url_doctorlist_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def doctorlist_delete(request,pk):
    doctorlist = get_object_or_404(DoctorList, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        doctorlist.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_doctorlists_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_doctorlists_list')

@login_required
def doctorlist_autocompletar(request):
    aux = request.GET.get('term', '')
    print("Valor do aux", aux)
    doctors = DoctorList.objects.filter(Q(name__icontains=aux) | Q(crm__icontains=aux))
    print("ate", aux)
    context = {'doctors': doctors }
    results = [] 
    
    for r in doctors:
        json = {}
        json['value'] = "{}, {}/{}".format(r.name,r.crm,r.state)
        json['id'] = r.id
        results.append(json)
    return JsonResponse(results, safe=False)


@login_required
def cid10_list(request):
    template_name = "doctorlist/cid10_list.html"
    title = "Lista CID-10"
    cids = Cid10.objects.all()    
    context = {
        'cids': cids,
        'title': title      
    }
    return render(request,template_name,context)

@login_required
def cid10_detail(request,pk):
    template_name = "doctorlist/cid10_detail.html"
    cid = get_object_or_404(Cid10,pk=pk)
    context = {
        'cid': cid
    }
    return render(request, template_name, context)

# AUTCOMPLETAR PARA PROCURAR O CID
@login_required
def cid10_autocomplete(request):
    cid = request.GET.get('term', '')
    cids = Cid10.objects.filter(category__icontains=cid)
    context = {'cids': cids }
    results = [] 
    
    for r in cids:
        json = {}
        json['value'] = r.category
        json['id'] = r.id
        results.append(json)
    return JsonResponse(results, safe=False)

def cid10_ajax(request):
    cid = request.GET.get('ff','')
    if Cid10.objects.filter(category=cid).exists():
        cid = Cid10.objects.get(category=cid)
        category = cid.category
        description = cid.description   
    else:
        category = ""
        description = "CID inválido."
    
    context = {'category': category, 'description': description }
    #context = {'category': cid.category, 'description': cid.description }
    #print("Categoria e descrição: {} - {}".format(cid.category.strip('\r').strip('\n'),cid.description.strip('\r').strip('\n')))
    return render(request, 'doctorlist/_cid10_ajax.html',context)
####### FIM DOCTORS LIST #########

###### AJAX PARA PROCURAR ESTADOS CIDADES #######

@login_required
def autocomplete_states(request):    
    if request.method == 'GET':
        q = request.GET.get('term', '')
        q = '%' + q + '%'        
        search_qs = States2.objects.raw(''' select 1 as id, city.name || ' / ' || s.uf as nome from statescity_states2 s
                                        inner join statescity_cities city on (s.id = city.uf::INTEGER) 
                                        where city.name ilike %s ''',[q])        
        results = []        
        for r in search_qs:
            r = r.nome.replace("'","").strip(" ")            
            results.append(r)        
    else:
        data = 'fail'
    mimetype = 'application/json'
    return JsonResponse(results, safe=False)

# AJAX PARA SELECTBOX EMPRESAS/DEPARTAMENTOS
def departments_choices_ajax(request):    
    company = request.GET.get('select_company')
    departments = Department.objects.filter(company_id=int(company))    
    context = {'departments': departments }
    return render(request, 'profilepersontype/_departments_choices.html',context)


# AJAX PARA CAMPOS INPUT PARA PROCURAR PESSOAS
def search_peoples(request):    
    people = request.GET.get('term', '')    
    peoples = Person.objects.filter(name__icontains=people)        
    context = {'peoples': peoples }
    results = [] 
    for r in peoples:
        json = {}
        json['value'] = r.name
        json['id'] = r.id
        results.append(json)
    return JsonResponse(results, safe=False)


