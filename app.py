from flask import Flask, render_template, request
import pandas as pd
import matplotlib
matplotlib.use('Agg')  # Cambiar backend de matplotlib
import matplotlib.pyplot as plt

app = Flask(__name__)

# Cargar datos desde el archivo CSV
archivo_csv = 'datos.csv'
datos = pd.read_csv(archivo_csv, sep=';')

# Limpiar espacios adicionales en los nombres de las columnas
datos.columns = datos.columns.str.strip()

# Ruta principal para mostrar tabla y gráfico
@app.route('/')
def index():
    # Convertir datos a HTML
    tabla = datos.to_html(index=False, classes='table table-striped')

     # Crear gráfico de puntos
    plt.figure(figsize=(10, 6))
    plt.bar(datos['Jugador'], datos['Puntos'], color='skyblue')
    plt.xlabel('Jugadores')
    plt.ylabel('Puntos')
    plt.title('Puntos por Jugador')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/grafico_puntos.png')  # Guardar gráfico en carpeta static
    plt.close()  # Limpia los gráficos para evitar superposición

    return render_template('index.html', tabla=tabla, grafico='static/grafico_puntos.png')


# Ruta para asistencias
@app.route('/asistencias')
def asistencias():
    # Crear gráfico de asistencias por jugador
    plt.figure(figsize=(10, 6))
    plt.bar(datos['Jugador'], datos['Asistencias'], color='orange')  # Asegúrate de que 'Asistencias' esté limpio
    plt.xlabel('Jugadores')
    plt.ylabel('Asistencias')
    plt.title('Asistencias por Jugador')
    plt.xticks(rotation=45, ha='right')
    plt.tight_layout()
    plt.savefig('static/grafico_asistencias.png')  # Guardar el gráfico
    plt.close()  # Limpia los gráficos para evitar superposición
    
    return render_template('asistencias.html', grafico='static/grafico_asistencias.png')

# Ruta para filtrar datos por equipo
@app.route('/filtrar', methods=['GET', 'POST'])
def filtrar():
    equipo = request.args.get('equipo', default=None)
    if equipo:
        datos_filtrados = datos[datos['Equipo'] == equipo]
        if datos_filtrados.empty:
            return render_template('filtro.html', tabla="No se encontraron resultados para ese equipo.")
    else:
        datos_filtrados = datos

    tabla = datos_filtrados.to_html(index=False, classes='table table-striped')
    return render_template('filtro.html', tabla=tabla)

if __name__ == '__main__':
    app.run(debug=True)
    
    
    