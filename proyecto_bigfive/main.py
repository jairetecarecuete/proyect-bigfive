from modelos import Test, Participante
from preguntas import cargar_preguntas
from analisis import calcular_promedios, mostrar_resultados, guardar_en_csv, grafica_resultados, generar_reporte_html
def main():
    nombre = input("¿Cual es tu nombre? ")
    participante = Participante(nombre)

    preguntas = cargar_preguntas()
    test = Test(preguntas)
    test.ejecutar(participante)

    promedios = calcular_promedios(participante)
    mostrar_resultados(promedios)
    guardar_en_csv(participante, promedios)
    grafica_resultados(promedios, "reportes/grafico.png")
    generar_reporte_html(participante, promedios, "grafico.png")
    print(f"\nResultados guardados en resultados.csv ")
    print("\nRespuestas por dimensión:")
    for dimension, valores in participante.respuestas.items():
        print(f"{dimension}: {valores}")
    
if __name__ == "__main__":
    main()
