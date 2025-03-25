import pandas as pd
import matplotlib.pyplot as plt

# Cargar el archivo CSV
archivo_csv = 'datos.csv'
datos = pd.read_csv(archivo_csv, sep=';')

# Limpiar datos (si es necesario)
datos.columns = datos.columns.str.strip()
datos['Jugador'] = datos['Jugador'].str.strip()
datos['Equipo'] = datos['Equipo'].str.strip()

# Corregir errores en nombres
datos.loc[datos['Jugador'] == 'Kylian Mbapp', 'Jugador'] = 'Kylian Mbappé'

# Crear gráfico de barras
plt.figure(figsize=(10, 6))
plt.bar(datos['Jugador'], datos['Puntos'], color='skyblue')
plt.xlabel('Jugadores')
plt.ylabel('Puntos')
plt.title('Puntos por Jugador')
plt.xticks(rotation=45, ha='right')  # Rotar etiquetas de jugadores para mejor visibilidad
plt.tight_layout()  # Ajustar espaciado
plt.show()