from flask import Blueprint, render_template, request, redirect, url_for
from .models import Persona, Materia   
from . import db

main = Blueprint('main', __name__)

def crear_materias_si_no_existen():
    nombres = ["Programación 1", "Programación 2", "Matemática", "Base de Datos", "Redes"]
    for nombre in nombres:
        if not Materia.query.filter_by(nombre=nombre).first():
            db.session.add(Materia(nombre=nombre))
    db.session.commit()

@main.route('/')
def index():
    personas = Persona.query.all()
    materias = Materia.query.all()

    return render_template('index.html', personas=personas, materias=materias)

@main.route('/crear', methods=['POST'])
def crear():
    nombre = request.form['nombre']
    apellido = request.form['apellido']
    dni = request.form['dni']
    materia_id = request.form['materia_id']


    nueva_persona = Persona(nombre=nombre, apellido=apellido, dni=dni, materia_id=materia_id)
    db.session.add(nueva_persona)
    db.session.commit()

    return redirect(url_for('main.index') + "?agregado=ok")

    #return redirect(url_for('main.index'))


@main.route('/eliminar/<int:id>')
def eliminar(id):
    persona = Persona.query.get_or_404(id)
    db.session.delete(persona)
    db.session.commit()

    return redirect(url_for('main.index') + "?eliminado=ok")
    #return redirect(url_for('main.index'))


# Rutas disponibles
# / → Lista todas las personas y muestra el formulario
# /crear → Guarda una nueva persona (POST)
# /eliminar/<id> → Elimina una persona por ID