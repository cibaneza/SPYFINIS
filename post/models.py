from django.db import models
from django.core.validators import FileExtensionValidator
# from ckeditor.fields import RichTextField
from tinymce.models import HTMLField

CATEGORY_CHOICES = [
        ('Actuación y Creación Teatral', 'Actuación y Creación Teatral'),
        ('Arquitectura', 'Arquitectura'),
        ('Auditoria', 'Auditoria'),
        ('Ciencias de la Familia', 'Ciencias de la Familia'),
        ('Derecho', 'Derecho'),
        ('Dirección y Gestión de Artes Culinarias', 'Dirección y Gestión de Artes Culinarias'),
        ('Diseño', 'Diseño'),
        ('Enfermería', 'Enfermería'),
        ('Ing. Civil en Informática', 'Ing. Civil en Informática'),
        ('Ing. Civil Industrial', 'Ing. Civil Industrial'),
        ('Ing. Comercial', 'Ing. Comercial'),
        ('Ing. Control de Gestión', 'Ing. Control de Gestión'),
        ('Kinesiología', 'Kinesiología'),
        ('Lic. en Artes Visuales', 'Lic. en Artes Visuales'),
        ('Lic. en Historia', 'Lic. en Historia'),
        ('Lic. en Literatura', 'Lic. en Literatura'),
        ('Lic. en Medicina', 'Lic. en Medicina'),
        ('Lic. en Nutrición y Dietética', 'Lic. en Nutrición y Dietética'),
        ('Odontología', 'Odontología'),
        ('Ped. en Educación Básica', 'Ped. en Educación Básica'),
        ('Ped. en Educación Parvularia', 'Ped. en Educación Parvularia'),
        ('Periodismo', 'Periodismo'),
        ('Psicología', 'Psicología'),
        ('Publicidad', 'Publicidad'),
    ]

AYUDANTE_CHOICES = [
    ('Profesor', 'Profesor'),
    ('Ayudante', 'Ayudante'),
]

class PostModel(models.Model):
    profe = models.CharField(max_length=100, unique=True)
    date_created = models.DateTimeField(auto_now_add=True)
    imagen = models.ImageField(default='default.jpg', upload_to='perfil_profesor', validators=[
                              FileExtensionValidator(['png', 'jpg'])])
    #contenido = models.TextField()
    # contenido = RichTextField()
    contenido = HTMLField()
    categoria = models.CharField(max_length=50, choices=CATEGORY_CHOICES ,default="category1")
    ayudante = models.CharField(max_length=50, choices = AYUDANTE_CHOICES, default="Profesor")

    class Meta:
        ordering = ('-date_created',)

    def __str__(self):
        return self.profe
