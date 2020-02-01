from django.contrib import admin
from .models import Religions,MaritalStatus,Patients

admin.site.register(Patients)
admin.site.register(Religions)
admin.site.register(MaritalStatus)
