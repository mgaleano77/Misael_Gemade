import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import os

class Actividad2:
    def __init__(self):
        self.ruta_resultados = "Resultados_actividad_2/"
        self.ruta_imagenes = os.path.join(self.ruta_resultados, "Imagenes_PNG/")

        # Crear las carpetas si no existen
        os.makedirs(self.ruta_resultados, exist_ok=True)
        os.makedirs(self.ruta_imagenes, exist_ok=True)

df = pd.DataFrame(columns=["# ejercicio", "resultado"])

def agregar_resultado(ejercicio, resultado):
    global df
    df.loc[len(df)] = [ejercicio, resultado]

# Punto 1
array1 = np.arange(10, 30)
agregar_resultado(1, str(array1))

# Punto 2
matriz_ones = np.ones((10, 10))
suma = np.sum(matriz_ones)
agregar_resultado(2, suma)

# Punto 3
array2 = np.random.randint(1, 11, 5)
array3 = np.random.randint(1, 11, 5)
producto = array2 * array3
agregar_resultado(3, str(producto))

# Punto 4
matriz_ij = np.random.randint(1, 10, (4, 4))
determinante = np.linalg.det(matriz_ij)
if determinante != 0:
    inversa = np.linalg.inv(matriz_ij)
    agregar_resultado(4, f"Inversa: {inversa}")
else:
    agregar_resultado(4, "La matriz no es invertible")

# Punto 5
array_random = np.random.random(100)
max_index = np.argmax(array_random)
min_index = np.argmin(array_random)
agregar_resultado(5, f"Máximo: {array_random[max_index]}, Índice: {max_index}")
agregar_resultado(5, f"Mínimo: {array_random[min_index]}, Índice: {min_index}")

# Punto 6
array_a = np.arange(3).reshape(3, 1)
array_b = np.arange(3).reshape(1, 3)
resultado_broadcast = array_a + array_b
agregar_resultado(6, str(resultado_broadcast))

# Punto 7
matriz_5x5 = np.random.randint(1, 10, (5, 5))
submatriz = matriz_5x5[1:3, 1:3]
agregar_resultado(7, str(submatriz))

# Punto 8
array_ceros = np.zeros(10)
array_ceros[3:7] = 5
agregar_resultado(8, str(array_ceros))

# Punto 9
matriz_3x3 = np.random.randint(1, 10, (3, 3))
matriz_invertida = matriz_3x3[::-1]
agregar_resultado(9, str(matriz_invertida))

# Punto 10
datos_random = np.random.random(10)
mayores_05 = datos_random[datos_random > 0.5]
agregar_resultado(10, str(mayores_05))

# Guardar el archivo CSV en la carpeta correcta
actividad = Actividad2()
csv_path = os.path.join(actividad.ruta_resultados, "resultados_actividad_2.csv")
df.to_csv(csv_path, index=False)
print(f"Los resultados han sido guardados en '{csv_path}'.")

# Generar y guardar imágenes en la carpeta correcta
def guardar_imagen(nombre):
    ruta_completa = os.path.join(actividad.ruta_imagenes, nombre)
    plt.savefig(ruta_completa)
    plt.close()
    print(f"Imagen guardada: {ruta_completa}")

# Punto 11
x = np.random.random(100)
y = np.random.random(100)
plt.scatter(x, y)
guardar_imagen("grafica_punto_11.png")

# Punto 12
x_vals = np.linspace(-2*np.pi, 2*np.pi, 100)
y_vals = np.sin(x_vals) + np.random.normal(0, 0.1, 100)
plt.scatter(x_vals, y_vals, label='y = sin(x) + ruido')
plt.plot(x_vals, np.sin(x_vals), color='red', label='y = sin(x)')
plt.legend()
guardar_imagen("grafica_punto_12.png")

# Punto 13
x_grid, y_grid = np.meshgrid(np.linspace(-5, 5, 50), np.linspace(-5, 5, 50))
z_grid = np.cos(x_grid) + np.sin(y_grid)
plt.contour(x_grid, y_grid, z_grid)
guardar_imagen("grafica_punto_13.png")

# Punto 14
x_d = np.random.randn(1000)
y_d = np.random.randn(1000)
plt.scatter(x_d, y_d, c=np.sqrt(x_d**2 + y_d**2), cmap='viridis')
plt.colorbar()
guardar_imagen("grafica_punto_14.png")

# Punto 15
plt.contourf(x_grid, y_grid, z_grid, cmap='coolwarm')
plt.colorbar()
guardar_imagen("grafica_punto_15.png")

# Punto 16
plt.scatter(x_vals, y_vals, label=r'$y = \sin(x) + ruido$', alpha=0.6)
plt.plot(x_vals, np.sin(x_vals), color='red', label=r'$y = \sin(x)$')
plt.xlabel("Eje X")
plt.ylabel("Eje Y")
plt.title("Gráfico de Dispersión")
plt.legend()
guardar_imagen("grafica_punto_16.png")

# Punto 17
data_hist = np.random.randn(1000)
plt.hist(data_hist, bins=30, alpha=0.7)
guardar_imagen("grafica_punto_17.png")

# Punto 18
data1 = np.random.normal(0, 1, 1000)
data2 = np.random.normal(3, 1, 1000)
plt.hist(data1, bins=30, alpha=0.5, label="Set 1")
plt.hist(data2, bins=30, alpha=0.5, label="Set 2")
plt.legend()
guardar_imagen("grafica_punto_18.png")

# Punto 19
plt.hist(data_hist, bins=10, alpha=0.5, label="10 bins")
plt.hist(data_hist, bins=30, alpha=0.5, label="30 bins")
plt.hist(data_hist, bins=50, alpha=0.5, label="50 bins")
plt.legend()
guardar_imagen("grafica_punto_19.png")

# Punto 20
plt.hist(data_hist, bins=30, alpha=0.7)
plt.axvline(np.mean(data_hist), color='red', linestyle='dashed', linewidth=2, label='Media')
plt.legend()
guardar_imagen("grafica_punto_20.png")

# Punto 21
plt.hist(data1, bins=30, alpha=0.5, color='blue', label="Set 1")
plt.hist(data2, bins=30, alpha=0.5, color='green', label="Set 2")
plt.legend()
guardar_imagen("grafica_punto_21.png")