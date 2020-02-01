from django.db import models
from django.contrib.auth.models import User


class Countries(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)    
    name_pt = models.CharField('Nome Portugês', max_length=100, blank=False)
    acronym = models.CharField('Sigla', max_length=100, blank=False)        
    bacen = models.CharField('Bacen', max_length=100, blank=False)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

class States2(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)    
    uf = models.CharField('UF', max_length=100, blank=False)
    ibge = models.CharField('IBGE', max_length=100, blank=False)        
    country = models.CharField('País', max_length=100, blank=False)
    ddd = models.CharField('DDD', max_length=100, blank=False)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        ordering = ["uf"]

    def __str__(self):
        return self.name


class Cities(models.Model):
    name = models.CharField('Nome', max_length=100, blank=False)    
    uf = models.CharField('UF', max_length=100, blank=False)
    ibge = models.CharField('IBGE', max_length=100, blank=False)        
    lat_lon = models.TextField('Latitude/Longitude', blank=False)    
    created_at = models.DateTimeField('Criado em',auto_now_add=True)
    update_at = models.DateTimeField('Atualizado em', auto_now=True)
