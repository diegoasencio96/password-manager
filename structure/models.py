from django.db import models
from utils.models import Audit
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your models here.


class Category(Audit):
    name = models.CharField(max_length=50, blank=False)


class AccessCredential(Audit):
    user = models.ForeignKey(User, verbose_name='Usuario', on_delete=models.CASCADE)
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name='Categoria', on_delete=models.CASCADE, help_text='Categoría de la credencial de acceso')
    name = models.CharField(max_length=100, verbose_name='Nombre', blank=False, help_text='Nombre para la credencial de acceso')
    url = models.URLField(max_length=100, verbose_name='URL', blank=True, help_text='URL del sitio (Opcional)')
    email = models.EmailField(max_length=100, verbose_name='Correo electrónico', blank=True, help_text='Opcional')
    username = models.CharField(max_length=100, verbose_name='Usuario', blank=False, help_text='Usuario del sistema')
    password = models.CharField(max_length=100, verbose_name='Contraseña', blank=False, help_text='Contraseña del sistema')
    pin = models.IntegerField(null=True, blank=True, verbose_name='PIN', help_text='Opcional')

    class Meta:
        verbose_name = 'Credencial de Acceso'
        verbose_name_plural = 'Credenciales de Acceso'

    def __str__(self):
        return f'{self.name}'
