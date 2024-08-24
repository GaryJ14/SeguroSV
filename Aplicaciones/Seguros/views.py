from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Registro,Cliente,Empresa, PostVenta, Seguimiento
from django.contrib import messages
from django.conf import settings
# Create your views here.

def index(request):    
    return render (request,"index.html")
def login(request):    
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        
        try:
            user = Registro.objects.get(email=email)
            if user.password == password:
                # Aquí podrías manejar la lógica de iniciar sesión correctamente
                messages.success(request, 'Inicio de sesión exitoso')
                return redirect('menu')  # Redirige a la página principal u otra página
            else:
                messages.error(request, 'Usuario y/o Contraseña incorrectos')
                return render (request,"login.html")
        except Registro.DoesNotExist:
            messages.error(request, 'El correo electrónico no está registrado')
    return render (request,"login.html")
def registro(request):    
    return render (request,"registro.html")
def menu(request):    
    return render (request,"menu.html")
def empresa(request):    
    return render (request,"empresa.html")
def guardarEmpresa(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        ci_representante = request.POST['ci_representante']
        ruc = request.POST['ruc']
        constitucion = request.POST['constitucion']

        # Manejo de archivo para la nómina de socios
        nomina = request.FILES.get('nomina')

        # Crear instancia del modelo Empresa
        empresa = Empresa(
            ci_representante=ci_representante,
            ruc=ruc,
            constitucion=constitucion,
            nomina=nomina
        )

        # Guardar en la base de datos
        empresa.save()
        messages.success(request, "Empresa registrada exitosamente.")
        # Redirigir a una página de éxito o a donde quieras
        return redirect('menu')  

    return render(request, 'empresa.html')
def cliente(request):    
    return render (request,"cliente.html")


def guardar_cliente(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        ci = request.POST['ci']
        licencia = request.POST['licencia']
        ci_conyugue = request.POST.get('ci_conyugue', '')
        disolucion_conyugal = request.POST.get('disolucion_conyugal', '')

        # Manejo de archivos
        pago_servicio = request.FILES.get('pago_servicio')
        formulario_vinculacion = request.FILES.get('formulario_vinculacion')

        # Crear instancia del modelo Cliente
        cliente = Cliente(
            ci=ci,
            licencia=licencia,
            ci_conyugue=ci_conyugue,
            disolucion_conyugal=disolucion_conyugal,
            pago_servicio=pago_servicio,
            formulario_vinculacion=formulario_vinculacion
        )

        # Guardar en la base de datos
        cliente.save()
        messages.success(request, "Cliente registrado exitosamente.")
        # Redirigir a una página de éxito o a donde quieras
        return redirect('menu')  # Cambia 'success_page' por el nombre de la vista que desees

    return render(request, 'cliente.html')

def seguimiento(request):    
    return render (request,"seguimiento.html")
def postventa(request):    
    return render (request,"postventa.html")
def guardarPostventa(request):
    if request.method == 'POST':
        # Manejo de archivo para la Póliza Digital
        poliza = request.FILES.get('poliza')
        
        # Obtener datos del formulario
        plan_pago = request.POST.get('plan-pago', '')
        novedades = request.POST.get('novedades', '')

        # Crear instancia del modelo PostVenta
        postventa = PostVenta(
            poliza=poliza,
            plan_pago=plan_pago,
            novedades=novedades
        )

        # Guardar en la base de datos
        postventa.save()
        messages.success(request, "Postventa registrado exitosamente.")
        
        # Redirigir a una página de éxito o a donde quieras
        return redirect('menu')  # Cambia 'success_page' por el nombre de la vista que desees

    return render(request, 'postventa.html')
def guardarRegistro(request):
    if request.method == 'POST':
        # Obtener los datos del formulario
        nombres = request.POST['nombres']
        apellidos = request.POST['apellidos']
        cedula = request.POST.get('cedula')
        fecha_nacimiento = request.POST['fecha_nacimiento']
        email = request.POST['email']
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        codigo_empresa = request.POST.get ('codigo_empresa')
        ciudad = request.POST.get('ciudad')
        cargo = request.POST.get('cargo')

        # Crear un nuevo registro
        nuevoRegistro = Registro.objects.create(
            nombres=nombres, 
            apellidos=apellidos,
            cedula=cedula,
            fecha_nacimiento=fecha_nacimiento,
            email=email,
            password=password, 
            confirm_password=confirm_password,
            codigo_empresa=codigo_empresa,
            ciudad=ciudad,
            cargo=cargo
        )
        
        messages.success(request, "Usuario registrado exitosamente.")
        return redirect('/')  # Redirige a otra página después del éxito
    
    return render(request, 'registro.html')  # Si es GET, simplemente muestra el formulario

def agregarSeguimiento(request):
    if request.method == 'POST':
        # Obtener datos del formulario
        fecha_nacimiento = request.POST.get('fechaNacimiento')
        estado_civil = request.POST.get('estadoCivil')
        ocupacion = request.POST.get('ocupacion')
        observaciones = request.POST.get('observaciones')

        # Crear instancia del modelo Seguimiento
        seguimiento = Seguimiento(
            fecha_nacimiento=fecha_nacimiento,
            estado_civil=estado_civil,
            ocupacion=ocupacion,
            observaciones=observaciones
        )

        # Guardar en la base de datos
        seguimiento.save()
        messages.success(request, "El seguimiento a sido registrado exitosamente.")
        # Redirigir a una página de éxito o a donde quieras
        return redirect('menu')  # Cambia 'success_page' por el nombre de la vista que desees

    return render(request, 'seguimiento.html')