import pandas as pd
import random
import time
import sys
import matplotlib.pyplot as plt
from itertools import cycle

def ruleta_visual(nombres):
    spinner = cycle(['|', '/', '-', '\\'])
    selected_name = ""
    for _ in range(random.randint(10, 30)):
        selected_name = random.choice(nombres)
        sys.stdout.write(f"\rSeleccionando: {selected_name} {next(spinner)}   ")
        sys.stdout.flush()
        time.sleep(0.1)
    sys.stdout.write(f"\rSeleccionado: {selected_name} ✔️\n")

def asignar_categorias(nombres):
    edades = ["Bebé", "Niño", "Adolescente", "Adulto Joven", "Adulto", "Tercera Edad"]
    regiones = ["Norte", "Centro", "Sur"]
    generos = ["Mujer", "Hombre"]
    
    resultados = []
    for nombre in nombres:
        ruleta_visual(nombres)
        edad = random.choice(edades)
        region = random.choice(regiones)
        genero = random.choice(generos)
        resultados.append([nombre, edad, region, genero])
    
    return pd.DataFrame(resultados, columns=["Student", "Edad", "Región", "Género"])

def graficar_resultados(df_resultado):
    fig, ax = plt.subplots(1, 3, figsize=(15, 5))
    df_resultado["Edad"].value_counts().plot(kind='bar', ax=ax[0], title="Distribución de Edades", color='blue')
    df_resultado["Región"].value_counts().plot(kind='bar', ax=ax[1], title="Distribución de Regiones", color='green')
    df_resultado["Género"].value_counts().plot(kind='bar', ax=ax[2], title="Distribución de Género", color='red')
    plt.tight_layout()
    plt.show()

def graficar_por_alumno(df_resultado):
    for _, row in df_resultado.iterrows():
        fig, ax = plt.subplots(figsize=(5, 3))
        categorias = ["Edad", "Región", "Género"]
        valores = [row["Edad"], row["Región"], row["Género"]]
        ax.bar(categorias, [1, 1, 1], color=["blue", "green", "red"], tick_label=valores)
        ax.set_title(f"Categorías de {row['Student']}")
        plt.show()

def main():
    # Cargar datos
    archivo_csv = "alumnos.csv"  # Nombre del archivo CSV
    df = pd.read_csv(archivo_csv)
    nombres = df['Student'].tolist()
    
    # Asignar categorías aleatorias
    df_resultado = asignar_categorias(nombres)
    
    # Mostrar resultados
    print(df_resultado)
    
    # Guardar en CSV
    df_resultado.to_csv("resultados_ruleta.csv", index=False)
    print("Resultados guardados en 'resultados_ruleta.csv'")
    
    # Graficar resultados generales
    graficar_resultados(df_resultado)
    
    # Graficar por alumno
    graficar_por_alumno(df_resultado)

if __name__ == "__main__":
    main()
