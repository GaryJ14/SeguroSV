from django.shortcuts import render, redirect
from django.shortcuts import get_object_or_404
from .models import Registro
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
def cliente(request):    
    return render (request,"cliente.html")
def seguimiento(request):    
    return render (request,"seguimiento.html")
def postventa(request):    
    return render (request,"postventa.html")
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

