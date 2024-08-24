from django.db import models

# Create your models here.
class Registro(models.Model):
    # ID autoincremental
    id = models.AutoField(primary_key=True)

    # Campos de texto
    nombres = models.CharField(max_length=255)
    apellidos = models.CharField(max_length=255)
    cedula = models.CharField(max_length=10)  # Se asume que la cédula es única
    fecha_nacimiento = models.DateField()
    email = models.EmailField(max_length=255)  # El email debe ser único
    password = models.CharField(max_length=255)
    confirm_password = models.CharField(max_length=255)  # Confirmar contraseña no suele ser necesario en el modelo

    # Campos de selección
    codigo_empresa = models.CharField(max_length=255)
    ciudad = models.CharField(max_length=255)
    cargo = models.CharField(max_length=50, choices=[
        ('desarrollador', 'Desarrollador'),
        ('diseñador', 'Diseñador'),
        ('analista', 'Analista'),
        # Agregar más opciones según sea necesario
    ])

    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} -{5} - {6} - {7} -{8} - {9}"
        return fila.format(self.id,self.nombres,self.apellidos,self.cedula,self.fecha_nacimiento,self.email,self.password,self.confirm_password,self.codigo_empresa,self.ciudad, self.cargo)
    