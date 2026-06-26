import statistics
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt

def guardar_en_csv(participante, promedios, ruta="resultados.csv"):
    existe = os.path.isfile(ruta)
    dimensiones = list(promedios.keys())

    with open(ruta, mode="a", newline="", encoding="utf-8") as archivo:
        escritor= csv.writer(archivo)

        #si el archivo no existe, escribimos el encabezado primero
        if not existe:
            encabezado = ["nombre", "fecha"] + dimensiones
            escritor.writerow(encabezado)

        fila = [participante.nombre, datetime.now().strftime("%Y-%m-%d %H:%M")]
        fila += [round(promedios[d], 2) for d in dimensiones]
        escritor.writerow(fila) 

def calcular_promedios(participante):
    """Recibe un participante y 
       devuelve un diccionario 
       {dimension: promedio}"""
    promedios = {}
    for dimension, valores in participante.respuestas.items():
        promedios[dimension] = statistics.mean(valores)
    return promedios

def mostrar_resultados(promedios):
    print("\n=== Resultados ===")
    for dimension, promedio in promedios.items():
        print(f"{dimension}: {promedio:.2f}")

def grafica_resultados(promedios, ruta_imagen="reportes/grafico.png"):
    os.makedirs(os.path.dirname(ruta_imagen), exist_ok=True)
    x = promedios.keys()
    y = promedios.values()

    plt.bar(x,y)
    
    plt.title("Tu escala Big Five")
    plt.xlabel("Modelos de personalidad")
    plt.ylabel("Puntajes 1-5")
    plt.ylim(bottom=1, top=5)
    plt.savefig(ruta_imagen)
    plt.close()

def generar_reporte_html(participante, promedios, ruta_imagen="grafico.png", carpeta="reportes"):
    os.makedirs(carpeta, exist_ok=True) #crea la carpeta si no existe

    filas_tabla = ""
    for dimension, promedio in promedios.items():
        filas_tabla += f"<tr><td>{dimension}</td><td>{promedio:.2f}</td></tr>\n"

    html = f"""
    <html>
    <head><title>Reporte Big Five - {participante.nombre}</title></head>
    <body>
        <h1>Resultados Big Five de {participante.nombre}</h1>
        <table border="1">
            <tr><th>Dimension</th><th>Puntaje (1-5)</th></tr>
            {filas_tabla}
        </table>
        <img src="{ruta_imagen}" alt="Grafico de resultados">
    </body>
    </html>
    """
    ruta_html = f"{carpeta}/reporte_{participante.nombre}.html"
    with open(ruta_html, "w", encoding="utf-8") as archivo:
        archivo.write(html)

    print(f"Reporte generado: {ruta_html}")    