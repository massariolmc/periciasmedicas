from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from django.contrib import messages
from .forms import UserCreate, UpdateUserForm, PasswordChangeUserForm
from PericiasMedicas.person.models import Person, ProfilePersonType, PersonType
from PericiasMedicas.company.models import Company, Department

@login_required
def home(request):
    #Antes de entrar faz o teste se o usuário possui um cadastro no Model Person.
    #Para logar, além de ter usuário no auth_user, tem que ter uma person criada
    verifica = Person.objects.filter(cpf=request.user.username).exists()
    if not verifica:
        logout(request)
        messages.warning(request, 'Usuário não possui cadastro. Contacte o administrador')
        return redirect('/accounts/login')

    template_name='core/home.html' 
    #person =  Department.objects.filter(profilepersontype__person__cpf=request.user.username)  
    # person = ProfilePersonType.objects.raw('''
    #     select * from person_profilepersontype pppt
    #     inner join company_department cd on (cd.id=pppt.department_id)
    #     inner join person_person pp on (pppt.person_id = pp.id)
    #     inner join person_persontype ppt on (pppt.person_type_id = ppt.id)
    #     where pp.cpf= %s
    # ''',[request.user.username])

    #ISSO TEM QUE SER COLOCADO LOGO APÓS LOGAR, PARA AS QUERYS SEREM EXECUTADO APENAS UMA VEZ.
    person = ProfilePersonType.objects.raw('''
        select * from person_profilepersontype pppt       
        inner join person_person pp on (pppt.person_id = pp.id)        
        where pp.cpf= %s
    ''',[request.user.username])
    person_department = ProfilePersonType.objects.raw('''
        select * from person_profilepersontype pppt
        inner join company_department cd on (cd.id=pppt.department_id)
        inner join person_person pp on (pppt.person_id = pp.id)        
        where pp.cpf= %s
    ''',[request.user.username])
    person_type = ProfilePersonType.objects.raw('''
        select * from person_profilepersontype pppt        
        inner join person_person pp on (pppt.person_id = pp.id)
        inner join person_persontype ppt on (pppt.person_type_id = ppt.id)
        where pp.cpf= %s
    ''',[request.user.username])

    #print("Valor do person", person)
    for pp in person:        
        #print("Valor do pp", pp.person_type.name)     
        request.session['person_id'] = pp.person.id
        request.session['person_name'] = pp.person.name
        request.session['profile_person_type_id'] = pp.id
        request.session['company_id'] = pp.department.company_id
    #print("Valor do person_deparement", person_department)
    aux = list()
    for pp in person_department:
        aux.append(pp.department.id)          
    request.session['department_id'] = aux    
    #print("Valor do person_type", person_type)
    aux = list()
    for pp in person_type:        
        aux.append(pp.person_type.id)
    request.session['type_name'] = aux
    return render(request,template_name,{'person':person})


@login_required
def signup(request):
    template_name = 'registration/signup.html'
    form = {}
    if request.method == 'POST':
        form = UserCreate(request.POST or None)
        if form.is_valid():
            form.save()
            return redirect('url_list_user')        
    else:
        form = UserCreate()
    return render(request, template_name, {'form': form})

@login_required
def list_user(request):
    template_name = 'registration/list_user.html'
    title = 'Lista de Usuários'
    users = User.objects.all
    return render(request, template_name, {'users': users , 'title': title})

@login_required
def edit_user(request,pk):
    template_name = 'registration/edit_user.html'
    form = {}
    user = get_object_or_404(User, pk=pk)
    user_form = user
    if request.method == 'POST':
        form = UpdateUserForm(request.POST or None, instance=user)        

        if form.is_valid():
            form.save()
            return redirect('url_detail_user', user.id)
    else:
        form = UpdateUserForm(instance=user)
    return render(request, template_name, {'form': form, 'user_form': user_form})

@login_required# Esse troca de senha foi customizado para trocar a senha sem estar logado, mas tem que saber a senha antiga
def password_change(request,pk):
    template_name = 'registration/custom_user_password_change.html'
    user = get_object_or_404(User, pk=pk)
    data = {}
    data['user'] = user
    if request.method == 'POST':        
        form = PasswordChangeUserForm(user=user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('url_detail_user', user.id)            
    else:
        form = PasswordChangeUserForm(user=user)
    data['form'] = form
    return render(request,template_name,data)
    
@login_required# Aqui esta customizado para usuário que não sabe a senha. Resseta e inseri uma senha padrão
def custom_resset_password(request,pk):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=pk)
        user.set_password('@1q2w3e4r@')
        user.save()
        messages.success(request, 'Senha ressetada com sucesso.')        
    return redirect('url_list_user')
@login_required
def detail_user(request,pk):    
    template_name = 'registration/detail_user.html'    
    user = get_object_or_404(User, pk=pk)
    return render(request, template_name, {'user': user})

@login_required
def disable_user(request,pk):    
    if request.method == 'GET':
        user = get_object_or_404(User, pk=pk)
        if user.is_active:
            user.is_active = False
            messages.success(request, 'Usuário desabilitado com sucesso.')
        else:
            user.is_active = True
            messages.success(request, 'Usuário habilitado com sucesso.')
        user.save()        
    return redirect('url_list_user')

@login_required
def super_user(request,pk):    
    if request.method == 'GET':
        user = get_object_or_404(User, pk=pk)
        if user.is_superuser:
            user.is_superuser = False
            messages.success(request, 'Perfil Super Usuário ativado com sucesso.')
        else:
            user.is_superuser = True
            messages.success(request, 'Perfil Super Usuário desativado com sucesso.')
        user.save()        
    return redirect('url_list_user')

@login_required
def staff_user(request,pk):
    if request.method == 'GET':
        user = get_object_or_404(User, pk=pk)
        if user.is_staff:
            user.is_staff = False
            messages.success(request, 'Perfil Super Usuário ativado com sucesso.')
        else:
            user.is_staff = True
            messages.success(request, 'Perfil Super Usuário desativado com sucesso.')
        user.save()        
    return redirect('url_list_user')

@login_required
def profile(request):
    template_name = 'core/profile.html'
    person = Person.objects.get(cpf=request.user.username)
    data = {
        'person': person
    }
    return render(request,template_name, data)
    
