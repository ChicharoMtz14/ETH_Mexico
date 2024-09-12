from flask import Flask, render_template

app = Flask(__name__, template_folder = 'Templates')

# Ruta para la pantalla de inicio
@app.route('/')
def index():
    return render_template('index.html')

# Ruta para el botón "Sobre el proyecto"
@app.route('/sobre')
def sobre():
    return render_template('sobre.html')

# Ruta para generar nueva votación (solo la interfaz por ahora)
@app.route('/nueva_votacion')
def nueva_votacion():
    return render_template('nueva_votacion.html')

# Ruta para consultar resultados previos (solo la interfaz por ahora)
@app.route('/resultados')
def resultados():
    return render_template('resultados.html')

@app.route('/equipo')
def equipo():
    return render_template('equipo.html')

@app.route('/votar')
def votar():
    return render_template('votar.html')

# Iniciar la aplicación
if __name__ == "__main__":
    app.run(debug=True)
