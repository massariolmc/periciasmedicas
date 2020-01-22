from django.urls import path
from . import views

urlpatterns = [   
    # PERSON
    path('people', views.people_list, name='url_people_list'),
    path('person-create', views.person_create, name='url_person_create'),    
    path('person/<int:pk>', views.person_detail, name='url_person_detail'),
    path('person/<int:pk>/edit', views.person_edit, name='url_person_edit'),
    path('person/<int:pk>/delete', views.person_delete, name='url_person_delete'),
    
    #PERSON TYPE
    path('persontypes', views.persontypes_list, name='url_persontypes_list'),
    path('persontype-create', views.persontype_create, name='url_persontype_create'),    
    path('persontype/<int:pk>', views.persontype_detail, name='url_persontype_detail'),
    path('persontype/<int:pk>/edit', views.persontype_edit, name='url_persontype_edit'),
    path('persontype/<int:pk>/delete', views.persontype_delete, name='url_persontype_delete'),

    #PROFILE PERSON TYPE
    path('profilepersontypes/<int:pk>', views.profilepersontypes_list, name='url_profilepersontypes_list'),
    path('profilepersontype-create/<int:pk>', views.profilepersontype_create, name='url_profilepersontype_create'),    
    path('profilepersontype_save', views.profilepersontype_save, name='url_profilepersontype_save'),    
    path('profilepersontype/<int:pk>', views.profilepersontype_detail, name='url_profilepersontype_detail'),
    path('profilepersontype/<int:pk>/edit', views.profilepersontype_edit, name='url_profilepersontype_edit'),
    path('profilepersontype/<int:pk>/delete', views.profilepersontype_delete, name='url_profilepersontype_delete'),

    #MEDICALSPECIALTY
    path('medicalspecialties/', views.medicalspecialties_list, name='url_medicalspecialties_list'),
    path('medicalspecialty-create/', views.medicalspecialty_create, name='url_medicalspecialty_create'),        
    path('medicalspecialty/<int:pk>', views.medicalspecialty_detail, name='url_medicalspecialty_detail'),
    path('medicalspecialty/<int:pk>/edit', views.medicalspecialty_edit, name='url_medicalspecialty_edit'),
    path('medicalspecialty/<int:pk>/delete', views.medicalspecialty_delete, name='url_medicalspecialty_delete'),

    #DOCTOR
    path('doctors/', views.doctors_list, name='url_doctors_list'),
    path('doctor-create/', views.doctor_create, name='url_doctor_create'),        
    path('doctor/<int:pk>', views.doctor_detail, name='url_doctor_detail'),
    path('doctor/<int:pk>/edit', views.doctor_edit, name='url_doctor_edit'),
    path('doctor/<int:pk>/delete', views.doctor_delete, name='url_doctor_delete'),

    #DOCTORLIST
    path('doctorlists/', views.doctorlists_list, name='url_doctorlists_list'),
    path('doctorlist-create/', views.doctorlist_create, name='url_doctorlist_create'),        
    path('doctorlist/<int:pk>', views.doctorlist_detail, name='url_doctorlist_detail'),
    path('doctorlist/<int:pk>/edit', views.doctorlist_edit, name='url_doctorlist_edit'),
    path('doctorlist/<int:pk>/delete', views.doctorlist_delete, name='url_doctorlist_delete'),
    path('doctorlist_autocompletar', views.doctorlist_autocompletar, name='url_doctorlist_autocompletar'),# Busca todos os Médicos Psiquiatras do MS por AJAX
    path('cid10_list/', views.cid10_list, name='url_cid10_list'),# LISTA TODOS OS CID-10
    path('list_cid10/<int:pk>', views.cid10_detail, name='url_cid10_detail'),
    path('doctorlist/cid10_autocomplete/', views.cid10_autocomplete, name='url_cid10_autocomplete'),#AUTCOMPLETAR PARA BUSCAR O CID
    path('doctorlist/cid10_ajax/', views.cid10_ajax, name='url_cid10_ajax'),#AJAX PARA BUSCAR O CID    


    path('people/search_peoples', views.search_peoples, name='url_search_peoples'),   
    path('people/autocomplete_states', views.autocomplete_states, name='url_states_search'),   
    path('profilepersontype/departments_choices_ajax', views.departments_choices_ajax, name='url_departments_choices_ajax'),   
]