from django.db import models

# Create your models here.

# Create your models here.
class Institucion(models.Model):
    institucion = models.CharField(max_length=60)
    direccion = models.CharField(max_length=60)

    def __str__(self):
        return self.institucion

class Grupo(models.Model):
    grupo = models.CharField(max_length=60)
    periodo = models.CharField(max_length=4)

    def __str__(self):
        return self.grupo

class Persona(models.Model):

    class Tipo_Documento(models.TextChoices):
        DNI = 'DNI', 'DNI'
        PASS = 'PASS' 'Pasaporte'

    class Estado_Persona(models.TextChoices):
        ACT = 'ACT', 'Activo'
        BAJA = 'BAJA' 'Baja'

    institucion = models.ForeignKey(
        Institucion, on_delete=models.CASCADE,
        related_name='persona_institucion'
    )

    apellido = models.CharField(max_length=60)
    nombre = models.CharField(max_length=60)
    tipo_documento = models.CharField(max_length=13,
                                      choices=Tipo_Documento.choices,
                                      default=Tipo_Documento.DNI)
    documento = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    fecha_nacimiento = models.DateTimeField
    direccion = models.TextField()
    email = models.EmailField
    estado = models.CharField(max_length=8,
                              choices=Estado_Persona.choices,
                              default=Estado_Persona.ACT)

    def __str__(self):
        return self.apellido