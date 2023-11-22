# Generated by Django 4.2.1 on 2023-06-23 20:05

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PostModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('profe', models.CharField(max_length=100, unique=True)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('imagen', models.ImageField(default='default.jpg', upload_to='perfil_profesor', validators=[django.core.validators.FileExtensionValidator(['png', 'jpg'])])),
                ('contenido', models.TextField()),
                ('categoria', models.CharField(choices=[('Actuación y Creación Teatral', 'Actuación y Creación Teatral'), ('Arquitectura', 'Arquitectura'), ('Auditoria', 'Auditoria'), ('Ciencias de la Familia', 'Ciencias de la Familia'), ('Derecho', 'Derecho'), ('Dirección y Gestión de Artes Culinarias', 'Dirección y Gestión de Artes Culinarias'), ('Diseño', 'Diseño'), ('Enfermería', 'Enfermería'), ('Ing. Civil en Informática', 'Ing. Civil en Informática'), ('Ing. Civil Industrial', 'Ing. Civil Industrial'), ('Ing. Comercial', 'Ing. Comercial'), ('Ing. Control de Gestión', 'Ing. Control de Gestión'), ('Kinesiología', 'Kinesiología'), ('Lic. en Artes Visuales', 'Lic. en Artes Visuales'), ('Lic. en Historia', 'Lic. en Historia'), ('Lic. en Literatura', 'Lic. en Literatura'), ('Lic. en Medicina', 'Lic. en Medicina'), ('Lic. en Nutrición y Dietética', 'Lic. en Nutrición y Dietética'), ('Odontología', 'Odontología'), ('Ped. en Educación Básica', 'Ped. en Educación Básica'), ('Ped. en Educación Parvularia', 'Ped. en Educación Parvularia'), ('Periodismo', 'Periodismo'), ('Psicología', 'Psicología'), ('Publicidad', 'Publicidad')], default='category1', max_length=50)),
            ],
            options={
                'ordering': ('-date_created',),
            },
        ),
    ]
