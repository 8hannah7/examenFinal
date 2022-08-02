from django.http import HttpResponse
from django.shortcuts import render, HttpResponse , redirect
from miapp.models import Course
from django.db.models import Q
from miapp.forms import FormCourse
from django.contrib import messages


# Create your views here.
layout = """
    <h1>Universidad Nacional Tecnologica De Lima Sur</h1>
    <hr/>
    <ul>
        <li>
            <a href="/cursos">Cursos</a>
        </li>
        <li>
            <a href="/crearcurso">Crear curso</a>
        </li>
        <li>
            <a href="/carreras">Carreras</a>
        </li>
        <li>
            <a href="/crearcarrera">Crear Carrera</a>
        </li>
    </ul>
    <hr/>

"""
def index(request):
    mensaje ="""
        <h1>Listado de Cursos</h1>
    """
    return render(request,'index.html')


def listar_course(request):
    course = Course.objects.all();
    """course = Course.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )"""
    return render(request, 'listar_course.html',{
        'titulo': 'Listado de Cursos'
    })
def listar_career(request):
    course = Career.objects.all();
    """course = Career.objects.filter(
        Q(titulo__contains="Py") |
        Q(titulo__contains="Hab")
    )"""
    return render(request, 'listar_course.html',{
        'titulo': 'Listado de Carreras'
    })

def eliminar_course(request, id):
    course = Course.objects.get(pk=id)
    Course.delete()
    return redirect('listar_course')
def eliminar_career(request, id):
    course = Course.objects.get(pk=id)
    Course.delete()
    return redirect('listar_career')


def crearcurso(request):
    mensaje ="""
    <h1>Agregar Curso</h1>
    """
    return render(request,'crearcurso.html')
def crearcareer(request):
    mensaje ="""
    <h1>Agregar Career</h1>
    """
    return render(request,'crearcareer.html')



def create_course(request):
    if request.method == 'POST':
        formulario = FormCourse(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            
            idcourse  = data_form.get('idcourse')
            code = data_form['code']
            name = data_form['name']
            hour = data_form['hour']
            state = data_form['state']
            course = Course(
            idcourse = idcourse,
            code = code,
            name = name,
            hour = hour,
            state = state
        )
        course.save()
        
        messages.success(request, f'Se agregó correctamente el artículo {course.id}')
        
        return redirect('listar_course')
        

    else:
        formulario = FormCourse()
        
 
    return render(request, 'create_course.html',{
        'form': formulario
    })

def create_career(request):
    if request.method == 'POST':
        formulario = FormCourse(request.POST)
        if formulario.is_valid():
            data_form = formulario.cleaned_data
            
            idcareer  = data_form.get('idcourse')
            name = data_form['name']
            shortname = data_form['shortname']
            image = data_form['hour']
            state = data_form['state']
            career= Course(
            idcareer = idcourse,
            name = name,
            shortname = shortname,
            hour = hour,
            state = state
        )
        course.save()
        
        messages.success(request, f'Se agregó correctamente la carrera {career.id}')
        
        return redirect('listar_career')
        

    else:
        formulario = FormCourse()
        
 
    return render(request, 'create_course.html',{
        'form': formulario
    })


def carreras(request):
    mensaje ="""
    <h1>Listado de Carreras</h1>
    """
    return render(request,'carreras.html')

def crearcarrera(request):
    mensaje ="""
    <h1>Agregar Carreras</h1>
    """
    return render(request,'crearcarrera.html')