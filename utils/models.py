from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Audit(models.Model):
    created_at = models.DateTimeField(verbose_name='Fecha de creación', auto_now_add=True)
    updated_at = models.DateTimeField(verbose_name='Fecha de modificación', blank=True, auto_now=True)

    class Meta:
        abstract = True