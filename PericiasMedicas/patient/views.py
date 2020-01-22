from django.shortcuts import render,get_object_or_404, redirect
from django.http import JsonResponse, HttpResponse
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from .form import PatientForm
from .models import Patients
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from PericiasMedicas.statescity.models import States2, Cities

@login_required
def patient_create(request):
    data = {}
    #form = PatientForm(request.POST or None)
    if request.method == 'POST':
        print("Entrei no method")
        form = PatientForm(request.POST)
        if form.is_valid():
            print("Entrei no is_valid")
            form.save()
            return redirect('url_patients_list')
        else:
            print("algo não está valido.")
    else:
        form = PatientForm()             
    
    data['form'] = form
    return render(request,'patients/form.html',data)

@login_required
def patients_list(request):
    template_name = "patients/list.html"
    patients = Patients.objects.all()
    
    context = {
        'patients': patients        
    }
    return render(request,template_name,context)

@login_required
def patient_detail(request, pk=None, *args, **kwargs):
    #print(args)
    #print(kwargs)
    #queryset = Patients.objects.get(pk=pk)
    template_name = "patients/detail.html"
    queryset = get_object_or_404(Patients,pk=pk)
    context = {
        'patient': queryset
    }
    return render(request, template_name, context)

@login_required
def patient_edit(request, pk):    
    template_name='patients/form.html'
    data = {}
    patient = get_object_or_404(Patients, pk=pk)    
    form = PatientForm(request.POST or None, instance=patient)
    if form.is_valid():            
        form.save()
        return redirect('url_patient_detail',pk=pk)    
    
    data['form'] = form
    return render(request,template_name,data)

@login_required
def patient_delete(request,pk):
    patient = get_object_or_404(Patients, pk=pk)
    print("request", request.method)
    if request.method == 'GET':        
        patient.delete()
        messages.success(request, 'Ação concluída com sucesso.')
        return redirect('url_patients_list')
    else:
        messages.warning(request, 'Ação não concluída.')
        return redirect('url_patients_list')

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
