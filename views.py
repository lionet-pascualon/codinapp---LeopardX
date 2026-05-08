from django.shortcuts import render
from django.http import HttpResponse
# Agrupamos todos los formularios y modelos arriba
from AppCoder.forms import CursoFormulario, ProfesorFormulario
from AppCoder.models import Curso, Profesor
from AppCoder.models import Estudiante # Asegurate que esté en los imports de arriba
from AppCoder.forms import EstudianteFormulario
# --- VISTAS DE NAVEGACIÓN ---

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def cursos(request):
    mis_cursos = Curso.objects.all() 
    return render(request, "AppCoder/cursos.html", {"cursos": mis_cursos})

def estudiantes(request):
    if request.method == "POST":
        mi_formulario = EstudianteFormulario(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            estudiante = Estudiante(nombre=info['nombre'], apellido=info['apellido'], email=info['email'])
            estudiante.save()
            return render(request, "AppCoder/exito.html")
    else:
        mi_formulario = EstudianteFormulario()

    todos = Estudiante.objects.all()
    return render(request, "AppCoder/estudiantes.html", {"mi_formulario": mi_formulario, "estudiantes": todos})

# --- SECCIÓN PROFESORES (LA NUEVA) ---

def profesores(request):
    if request.method == "POST":
        mi_formulario = ProfesorFormulario(request.POST)
        if mi_formulario.is_valid():
            info = mi_formulario.cleaned_data
            profe = Profesor(nombre=info['nombre'], apellido=info['apellido'], 
                             email=info['email'], profesion=info['profesion'])
            profe.save()
            return render(request, "AppCoder/exito.html")
    else:
        mi_formulario = ProfesorFormulario()

    todos = Profesor.objects.all()
    return render(request, "AppCoder/profesores.html", {"mi_formulario": mi_formulario, "profesores": todos})

# --- FORMULARIOS Y BÚSQUEDA ---

def curso_formulario(request):
    if request.method == "POST":
        mi_formulario = CursoFormulario(request.POST)
        if mi_formulario.is_valid():
            informacion = mi_formulario.cleaned_data
            curso = Curso(nombre=informacion['nombre'], camada=informacion['camada'])
            curso.save()
            return render(request, "AppCoder/exito.html") 
    else:
        mi_formulario = CursoFormulario()
    
    return render(request, "AppCoder/curso_formulario.html", {"mi_formulario": mi_formulario})

def busqueda_camada(request):
    return render(request, "AppCoder/busqueda_camada.html")

def buscar(request):
    if request.GET.get("camada"):
        camada = request.GET["camada"]
        cursos_encontrados = Curso.objects.filter(camada__icontains=camada)
        return render(request, "AppCoder/resultado_busqueda.html", {"cursos": cursos_encontrados, "camada": camada})
    else:
        return HttpResponse("No enviaste datos")


# --- ESTAS COSAS NO SE USARAN PERO QUEDARAN POR SI LAS DUDAS ---        