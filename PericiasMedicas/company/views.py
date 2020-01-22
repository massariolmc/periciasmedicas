from django.shortcuts import render,get_object_or_404, get_list_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PericiasMedicas.statescity.models import States2, Cities
from .forms import CompanyForm, DepartmentForm
from .models import Company, Department
from crispy_forms.utils import render_crispy_form
from django.template.context_processors import csrf

####### COMPANY
def company_create(request):
    template_name = 'company/form.html'    
    data = {}
    data['title'] = "Cadastro de Empresas"
    if request.method == 'POST':        
        form = CompanyForm(request.POST)
        if form.is_valid():            
            form.save()                    
            return redirect('url_companies_list')
        else:
            print("algo não está valido.")
    else:
        form = CompanyForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def companies_list(request):
    template_name = "company/list.html"
    companies = Company.objects.all()    
    context = {
        'companies': companies,
        'title': "Empresas Cadastradas"       
    }
    return render(request,template_name,context)

@login_required
def company_detail(request, pk=None,):
    template_name = "company/detail.html"
    company = get_object_or_404(Company,pk=pk)
    context = {
        'company': company
    }
    return render(request, template_name, context)

@login_required
def company_edit(request, pk):    
    template_name='company/form.html'
    data = {}    
    company = get_object_or_404(Company, pk=pk)        
    user_created = company.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = CompanyForm(request.POST or None, instance=company)
    if form.is_valid():
        company = form.save(commit=False)
        company.user_created = user_created
        company.save()
        return redirect('url_company_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def company_delete(request,pk):
    company = get_object_or_404(Company, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        company.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_companies_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_companies_list')
########### FIM COMPANY############################

########   DEPARTMENT   #####################

def department_create(request,pk):
    template_name = 'department/form.html'
    company = Company.objects.get(pk=pk)
    title1 = "Empresa: "
    title2 = 'Cadastro de Departamentos'           
    data = {
        'title1': title1,
        'title2': title2,
        'company_name': company.name,
        'company_id': company.id,
    }
    
    if request.method == 'POST':        
        form = DepartmentForm(request.POST)
        if form.is_valid():            
            form.save()                    
            return redirect('url_show_departments_company',company.id)            
        else:
            print("algo não está valido.")
    else:
        form = DepartmentForm()             
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def departments_list(request):
    template_name = "department/list.html"
    departments = Department.objects.all()    
    context = {
        'departments': departments,
        'title': "Departamentos Cadastrados"       
    }
    return render(request,template_name,context)

@login_required
def department_detail(request, pk=None,):
    template_name = "department/detail.html"
    department = get_object_or_404(Department,pk=pk)
    context = {
        'department': department
    }
    return render(request, template_name, context)

@login_required
def department_edit(request, pk):    
    template_name='department/form.html'    
    department = get_object_or_404(Department, pk=pk)        
    company = Company.objects.get(pk=department.company_id)
    print("Passei daqui2")
    title1 = "Empresa: "
    title2 = 'Cadastro de Departamentos'           
    data = {
        'title1': title1,
        'title2': title2,
        'company_name': company.name,
        'company_id': company.id,
    }   
    user_created = department.user_created # Esta linha faz com que o user_created não seja modificado, para mostrar quem criou esta pessoa
    form = DepartmentForm(request.POST or None, instance=department)
    if form.is_valid():
        department = form.save(commit=False)
        department.user_created = user_created
        department.save()
        return redirect('url_department_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def department_delete(request,pk):
    department = get_object_or_404(Department, pk=pk)
    company_id = department.company_id
    print("request", request.method)
    if request.method == 'GET':        
        department.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_show_departments_company', company_id)
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_show_departments_company', company_id)


####### FIM DEPARTMENT ######################


########### GENERIC ########################
@login_required
def autocomplete_states(request):    
    if request.method == 'GET':
        print("encondig", request.encoding)
        print("Valor da request", request.GET)
        print("entrei no GET")               
        q = request.GET.get('term', '')                
        print("Valor do q",q)
        q = '%' + q + '%'        
        search_qs = States2.objects.raw(''' select 1 as id, city.name || ' / ' || s.uf as nome from statescity_states2 s
                                        inner join statescity_cities city on (s.id = city.uf::INTEGER) 
                                        where city.name ilike %s ''',[q])        
        results = []        
        for r in search_qs:
            r = r.nome.replace("'","").strip(" ")            
            results.append(r)        
    else:
        print("entrei no ELSE")
        data = 'fail'
    mimetype = 'application/json'
    return JsonResponse(results, safe=False)

@login_required
def show_departments_company(request,pk):
    template_name = "department/list.html"
    if request.method == 'GET':        
        title = "Departamentos da Empresa "
        #departments = Department.objects.filter(pk=pk)
        company = Company.objects.get(pk=pk)
        context = {                
                'title': title,          
                'company_name': company.name,
                'company_id': company.id
            }
        exists_departments = Department.objects.filter(company_id=pk).exists()
        if exists_departments:     
            departments = get_list_or_404(Department,company_id=pk)        
            context['departments'] = departments
        else:
            messages.warning(request, 'Crie um departamento.')
            context['departments'] = {}        
        
        return render(request, template_name, context)
    else:
        messages.warning(request, 'Contacte o Administrador.')
        return redirect('url_companies_list')

