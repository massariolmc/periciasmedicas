from django.urls import path
from . import views

urlpatterns = [
    #AuthorityRequesting
    path('authorityrequesting/', views.authorityrequesting_list, name='url_authorityrequesting_list'),
    path('authorityrequesting-create/', views.authorityrequesting_create, name='url_authorityrequesting_create'),        
    path('authorityrequesting/<int:pk>', views.authorityrequesting_detail, name='url_authorityrequesting_detail'),
    path('authorityrequesting/<int:pk>/edit', views.authorityrequesting_edit, name='url_authorityrequesting_edit'),
    path('authorityrequesting/<int:pk>/delete', views.authorityrequesting_delete, name='url_authorityrequesting_delete'),

    #locationobjective
    path('locationobjectives/', views.locationobjectives_list, name='url_locationobjectives_list'),
    path('locationobjective-create/', views.locationobjective_create, name='url_locationobjective_create'),        
    path('locationobjective/<int:pk>', views.locationobjective_detail, name='url_locationobjective_detail'),
    path('locationobjective/<int:pk>/edit', views.locationobjective_edit, name='url_locationobjective_edit'),
    path('locationobjective/<int:pk>/delete', views.locationobjective_delete, name='url_locationobjective_delete'),

    #ForensicScan
    path('forensicscans/', views.forensicscans_list, name='url_forensicscans_list'),
    path('forensicscan-create/', views.forensicscan_create, name='url_forensicscan_create'),        
    path('forensicscan/<int:pk>', views.forensicscan_detail, name='url_forensicscan_detail'),
    path('forensicscan/<int:pk>/edit', views.forensicscan_edit, name='url_forensicscan_edit'),
    path('forensicscan/<int:pk>/delete', views.forensicscan_delete, name='url_forensicscan_delete'),

    #NatureOfAction
    path('natureofactions/', views.natureofactions_list, name='url_natureofactions_list'),
    path('natureofaction-create/', views.natureofaction_create, name='url_natureofaction_create'),        
    path('natureofaction/<int:pk>', views.natureofaction_detail, name='url_natureofaction_detail'),
    path('natureofaction/<int:pk>/edit', views.natureofaction_edit, name='url_natureofaction_edit'),
    path('natureofaction/<int:pk>/delete', views.natureofaction_delete, name='url_natureofaction_delete'),

    #ReportStatus
    path('reportstatus/', views.reportstatus_list, name='url_reportstatus_list'),
    path('reportstatus-create/', views.reportstatus_create, name='url_reportstatus_create'),        
    path('reportstatus/<int:pk>', views.reportstatus_detail, name='url_reportstatus_detail'),
    path('reportstatus/<int:pk>/edit', views.reportstatus_edit, name='url_reportstatus_edit'),
    path('reportstatus/<int:pk>/delete', views.reportstatus_delete, name='url_reportstatus_delete'),

    #DiscussionConclusion
    path('discussionconclusions/', views.discussionconclusions_list, name='url_discussionconclusions_list'),
    path('discussionconclusion-create/', views.discussionconclusion_create, name='url_discussionconclusion_create'),        
    path('discussionconclusion/<int:pk>', views.discussionconclusion_detail, name='url_discussionconclusion_detail'),
    path('discussionconclusion/<int:pk>/edit', views.discussionconclusion_edit, name='url_discussionconclusion_edit'),
    path('discussionconclusion/<int:pk>/delete', views.discussionconclusion_delete, name='url_discussionconclusion_delete'),
    path('discussionconclusion/deleteall', views.discussionconclusion_delete_all, name='url_discussionconclusion_delete_all'),

    #CidNumber
    path('cidnumbers/<int:report_id>', views.cidnumbers_list, name='url_cidnumbers_list'),
    path('cidnumber-create/', views.cidnumber_create, name='url_cidnumber_create'),        
    path('cidnumber/<int:pk>', views.cidnumber_detail, name='url_cidnumber_detail'),
    path('cidnumber/<int:pk>/edit', views.cidnumber_edit, name='url_cidnumber_edit'),
    path('cidnumber/<int:pk>/delete', views.cidnumber_delete, name='url_cidnumber_delete'),

    #Report
    path('reports/', views.reports_list, name='url_reports_list'),
    path('report-create/', views.report_create, name='url_report_create'),        
    path('report/<int:pk>', views.report_detail, name='url_report_detail'),
    path('report/<int:pk>/edit', views.report_edit, name='url_report_edit'),
    path('report/<int:pk>/delete', views.report_delete, name='url_report_delete'),
    path('report/<int:pk>/valid', views.valid_report_item, name='url_valid_report_item'),
    path('report/<int:pk>/cancel', views.cancelar_report, name='url_cancelar_report'),
    path('report/<int:pk>/search_reports/', views.search_reports, name='url_search_reports'),    
    path('report/<int:pk>/print_docx/', views.print_docx, name='url_print_docx'),    
    path('report/<int:pk>/print_pdf/', views.print_pdf, name='url_print_pdf'),    
    path('report/report_location_objective', views.get_report_location_objective, name='url_report_location_objective'),# ESTE É UM AJAX
    path('report/forensic_copy_report', views.forensic_copy_report, name='url_forensic_copy_report'),# ESTE É UM AJAX

    #MedicalDocument
    path('medicaldocuments/', views.medicaldocuments_list, name='url_medicaldocuments_list'),
    path('medicaldocument-create/', views.medicaldocument_create, name='url_medicaldocument_create'),        
    path('medicaldocument/<int:pk>/delete', views.medicaldocument_delete, name='url_medicaldocument_delete'),

    #TypeItem
    path('typeitems/', views.typeitems_list, name='url_typeitems_list'),
    path('typeitem-create/', views.typeitem_create, name='url_typeitem_create'),        
    path('typeitem/<int:pk>', views.typeitem_detail, name='url_typeitem_detail'),
    path('typeitem/<int:pk>/edit', views.typeitem_edit, name='url_typeitem_edit'),
    path('typeitem/<int:pk>/delete', views.typeitem_delete, name='url_typeitem_delete'),

    #TypeItemByNatureOfAction
    path('typeitembynatureofactions/', views.typeitembynatureofactions_list, name='url_typeitembynatureofactions_list'),
    path('typeitembynatureofaction-create/', views.typeitembynatureofaction_create, name='url_typeitembynatureofaction_create'),        
    path('typeitembynatureofaction/<int:pk>', views.typeitembynatureofaction_detail, name='url_typeitembynatureofaction_detail'),
    path('typeitembynatureofaction/<int:pk>/edit', views.typeitembynatureofaction_edit, name='url_typeitembynatureofaction_edit'),
    path('typeitembynatureofaction/<int:pk>/delete', views.typeitembynatureofaction_delete, name='url_typeitembynatureofaction_delete'),
    path('typeitembynatureofaction/deleteall', views.typeitembynatureofaction_delete_all, name='url_typeitembynatureofaction_delete_all'),

    #Item2
    path('items2/<int:report>/<int:type_item>', views.items2_list, name='url_items2_list'),    
    path('item2-create/<int:report>/<int:type_item>', views.item2_create, name='url_item2_create'),
    #path('item2_check_report/<int:report>/<int:type_item>', views.item2_check_report, name='url_item2_check_report'),
    path('copy_item_report/<int:report>/<int:type_item>', views.copy_item_report, name='url_copy_item_report'),
    path('item2/<int:pk>', views.item2_detail, name='url_item2_detail'),
    path('item2/<int:pk>/item2_answer', views.item2_answer, name='url_item2_answer'),
    path('item2/<int:pk>/edit', views.item2_edit, name='url_item2_edit'),
    path('item2/<int:pk>/delete', views.item2_delete, name='url_item2_delete'),
    path('item_check_report/<int:report>/<int:type_item>', views.item_check_report, name='url_item_check_report'),
    path('report/itembynatureaction_copy_item', views.itembynatureaction_copy_item, name='url_itembynatureaction_copy_item'),# ESTE É UM AJAX
    path('item2/delete_all', views.item2_delete_all, name='url_item2_delete_all'),
    
    
    #ItemsAnswer
    path('itemsanswers/', views.itemsanswers_list, name='url_itemsanswers_list'),
    path('itemsanswer-create/', views.itemsanswer_create, name='url_itemsanswer_create'),        
    path('itemsanswer/<int:pk>', views.itemsanswer_detail, name='url_itemsanswer_detail'),
    path('itemsanswer/<int:pk>/edit', views.itemsanswer_edit, name='url_itemsanswer_edit'),
    path('itemsanswer/<int:pk>/delete', views.itemsanswer_delete, name='url_itemsanswer_delete'),
   
]