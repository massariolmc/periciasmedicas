from django.contrib import admin
from .models import Company, CompanyTaxRegime, CompanyType, Department
# Register your models here.
admin.site.register(Company)
admin.site.register(CompanyType)
admin.site.register(CompanyTaxRegime)
admin.site.register(Department)