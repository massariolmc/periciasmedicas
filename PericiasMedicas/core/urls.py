from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='url_signup'),
    path('list_user/', views.list_user, name='url_list_user'),
    path('edit_user/<int:pk>', views.edit_user, name='url_edit_user'),
    path('password_change/<int:pk>', views.password_change, name='url_password_change'),
    path('custom_resset_password/<int:pk>', views.custom_resset_password, name='url_custom_resset_password'),
    path('detail_user/<int:pk>', views.detail_user, name='url_detail_user'),
    path('disable_user/<int:pk>', views.disable_user, name='url_disable_user'),
    path('super_user/<int:pk>', views.super_user, name='url_super_user'),
    path('staff_user/<int:pk>', views.staff_user, name='url_staff_user'),
    path('profile/', views.profile, name='url_profile'),
]