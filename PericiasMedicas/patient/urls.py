from django.urls import path
from . import views

urlpatterns = [    
    path('patients', views.patients_list, name='url_patients_list'),
    path('patient-create', views.patient_create, name='url_patient_create'),    
    path('patient/<int:pk>', views.patient_detail, name='url_patient_detail'),
    path('patient/<int:pk>/edit', views.patient_edit, name='url_patient_edit'),
    path('patient/<int:pk>/delete', views.patient_delete, name='url_patient_delete'),
    path('patient/autocomplete_states', views.autocomplete_states, name='url_states_search'),       
   
]