from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('signup/', views.signup, name='url_signup'),
    path('list_user/', views.list_user, name='url_list_user'),
    path('edit_user/<int:pk>', views.edit_user, name='url_edit_user'),
    path('detail_user/<int:pk>', views.detail_user, name='url_detail_user'),
    path('profile/', views.profile, name='url_profile'),
]