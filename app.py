from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/estudiantes')
def estudiantes():
    data = [
        {"matricula": "2307001", "nombre": "Gerardo", "apellido_paterno": "Mathus", "apellido_materno": "Gómez Sandoval"},
        {"matricula": "2307002", "nombre": "Alberto", "apellido_paterno": "Preciado", "apellido_materno": "Fernández"},
        {"matricula": "2307003", "nombre": "Elsa", "apellido_paterno": "Serrano", "apellido_materno": "Salcedo"},
        {"matricula": "2307004", "nombre": "Isabel", "apellido_paterno": "López", "apellido_materno": "Acero"},
        {"matricula": "2402058", "nombre": "Raúl", "apellido_paterno": "Olivera", "apellido_materno": "Lara"}
    ]
    return render_template('estudiantes.html', data=data)

@app.route('/materias')
def materias():
    dato = [
        {"ID": "1101", "Nombre de la materia": "Matematicas", "Horario": "08:00 - 09:00", "Profesor": "Gerardo Mathus"},
        {"ID": "1102", "Nombre de la materia": "Historia", "Horario": "10:00 - 11:00", "Profesor": "Anabel Díaz"},
        {"ID": "1103", "Nombre de la materia": "Biologia", "Horario": "11:00 - 12:00", "Profesor": "Eduardo Basurto"},
        {"ID": "1104", "Nombre de la materia": "Fisica", "Horario": "12:00 - 13:00", "Profesor": "Dominica Ferrís"},
        {"ID": "1105", "Nombre de la materia": "Quimica", "Horario": "13:00 - 14:00", "Profesor": "Luis Dominguez"}
    ]
    return render_template('materias.html', dato=dato)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8888, debug=True)
