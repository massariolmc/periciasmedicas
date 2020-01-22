from django.urls import path
from . import views

urlpatterns = [ 
    #COMPANY   
    path('companies', views.companies_list, name='url_companies_list'),
    path('company-create', views.company_create, name='url_company_create'),    
    path('company/<int:pk>', views.company_detail, name='url_company_detail'),
    path('company/<int:pk>/edit', views.company_edit, name='url_company_edit'),
    path('company/<int:pk>/delete', views.company_delete, name='url_company_delete'),
    # DEPARTMENT
    path('departments', views.departments_list, name='url_departments_list'),
    path('department-create/<int:pk>', views.department_create, name='url_department_create'),    
    path('department/<int:pk>', views.department_detail, name='url_department_detail'),
    path('department/<int:pk>/edit', views.department_edit, name='url_department_edit'),
    path('department/<int:pk>/delete', views.department_delete, name='url_department_delete'),

    #GENERIC
    path('company/show_departments_company/<int:pk>', views.show_departments_company, name='url_show_departments_company'),
    path('company/autocomplete_states', views.autocomplete_states, name='url_states_search'),   
]