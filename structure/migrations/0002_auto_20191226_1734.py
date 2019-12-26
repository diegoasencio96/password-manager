# Generated by Django 2.2.8 on 2019-12-26 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('structure', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='accesscredential',
            name='category',
            field=models.ForeignKey(blank=True, help_text='Categoría de la credencial de acceso', on_delete=django.db.models.deletion.CASCADE, to='structure.Category', verbose_name='Categoria'),
        ),
        migrations.AlterField(
            model_name='accesscredential',
            name='pin',
            field=models.IntegerField(blank=True, help_text='Opcional', null=True, verbose_name='PIN'),
        ),
    ]
