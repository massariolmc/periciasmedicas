from django.db import models

class TimeStampedModel(models.Model):
	created_at = models.DateTimeField(
        'criado em', 
        auto_now_add=True, 
        auto_now=False)
	updated_at = models.DateTimeField(
        'atualizado em', 
        auto_now_add=False, 
        auto_now=True)

	class Meta:
		abstract = True
