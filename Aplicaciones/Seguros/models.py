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

class Cliente(models.Model):
    # ID autoincremental
    id = models.AutoField(primary_key=True)
    # Campo de texto para CI
    ci = models.CharField(max_length=20, unique=True)
    
    # Campo de selección para Licencia
    LICENCIA_CHOICES = [
        ('tipo1', 'Tipo 1'),
        ('tipo2', 'Tipo 2'),
        ('tipo3', 'Tipo 3'),
        # Agrega más opciones según sea necesario
    ]
    licencia = models.CharField(max_length=10, choices=LICENCIA_CHOICES)
    
    # Campo de archivo para Pago de Servicio Básico
    pago_servicio = models.FileField(upload_to='pagos_servicios',null=True,blank=True)
    
    # Campo de texto para CI del Cónyuge
    ci_conyugue = models.CharField(max_length=20, null=True, blank=True)
    
    # Campo de texto para Disolución Conyugal
    disolucion_conyugal = models.CharField(max_length=255, null=True, blank=True)
    
    # Campo de archivo para Formulario de Vinculación
    formulario_vinculacion = models.FileField(upload_to='clientes',null=True,blank=True)
    
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4} -{5}"
        return fila.format(self.id,self.ci,self.licencia,self.pago_servicio,self.ci_conyugue,self.disolucion_conyugal, self.formulario_vinculacion)


class Empresa(models.Model):
    # ID autoincremental
    id = models.AutoField(primary_key=True)
    
    # Campo de texto para CI del Representante Legal
    ci_representante = models.CharField(max_length=20, unique=True)
    
    # Campo de texto para RUC
    ruc = models.CharField(max_length=13, unique=True)  # Asumiendo que el RUC es único y tiene una longitud de 13 caracteres
    
    # Campo de texto para Constitución de Empresa
    constitucion = models.CharField(max_length=255)
    
    # Campo de archivo para Nómina de Socios
    nomina = models.FileField(upload_to='nominas_socios')
    
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id,self.ci_representante,self.ruc,self.constitucion,self.nomina)


class PostVenta(models.Model):
    # ID autoincremental
    id = models.AutoField(primary_key=True)
    # Campo de archivo para Póliza Digital
    poliza = models.FileField(upload_to='polizas_digitales/')
    # Campo de selección para Plan de Pago
    PLAN_PAGO_CHOICES = [
        ('plan1', 'Plan Básico'),
        ('plan2', 'Plan Estándar'),
        ('plan3', 'Plan Premium'),
    ]
    plan_pago = models.CharField(max_length=10, choices=PLAN_PAGO_CHOICES)
    
    # Campo de texto para Novedades
    novedades = models.TextField(blank=True, null=True)
    def __str__(self):
        fila="{0}: {1} - {2} - {3}"
        return fila.format(self.id,self.poliza,self.plan_pago,self.novedades)


class Seguimiento(models.Model):
    # ID autoincremental
    id = models.AutoField(primary_key=True)
    
    # Campo de fecha para Fecha de Nacimiento
    fecha_nacimiento = models.DateField()
    
    # Campo de selección para Estado Civil
    ESTADO_CIVIL_CHOICES = [
        ('soltero', 'Soltero'),
        ('casado', 'Casado'),
        ('divorciado', 'Divorciado'),
        ('viudo', 'Viudo'),
    ]
    estado_civil = models.CharField(max_length=10, choices=ESTADO_CIVIL_CHOICES)
    
    # Campo de texto para Ocupación
    ocupacion = models.CharField(max_length=255)
    
    # Campo de texto para Observaciones
    observaciones = models.TextField()
    
    def __str__(self):
        fila="{0}: {1} - {2} - {3} - {4}"
        return fila.format(self.id,self.fecha_nacimiento,self.estado_civil,self.ocupacion,self.observaciones)

