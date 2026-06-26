#    proyecto_bigfive/
#    ├── main.py            punto de entrada, corre el programa <---
#    ├── modelos.py         clases Pregunta, Test, Participante
#    ├── preguntas.py       lista de preguntas Big Five (datos)
#    ├── analisis.py        cálculos estadísticos y gráficos
#    ├── resultados.csv     se genera al correr el programa
#    └── reportes/          (Etapa 2) acá irán los .html generados

class Pregunta:
    def __init__(self, texto, dimension):
        self.texto = texto
        self.dimension = dimension #ej: "apertura"
        self.respuesta = None  # Inicialmente sin respuesta

    def hacer_pregunta(self):
        print(f"\n{self.texto}") #
        while True:
            try:
                valor = int(input("Tu respuesta: "
                                "\n 1= Muy en desacuerdo"
                                "\n 2= En desacuerdo"
                                "\n 3= Neutral"
                                "\n 4= De acuerdo"
                                "\n 5= Muy de acuerdo "
                                "\n "))
                if 1 <= valor <= 5:
                    self.respuesta = valor
                    break
                else: 
                    print("Por favor ingresa un número entre 1 y 5.")
            except ValueError:
                print("Eso no es un numero válido.")

class Participante: 
    def __init__(self, nombre):
        self.nombre = nombre
        self.respuestas ={} # dimension -> lista de respuestas

    def agregar_respuesta(self, dimension, valor):
        self.respuestas.setdefault(dimension, []).append(valor)

class Test:
    def __init__(self, preguntas):
        self.preguntas = preguntas # lista de objetos Pregunta

    def ejecutar(self, participante):
        print(f"\n--- Test Big Five para {participante.nombre} ---")
        for pregunta in self.preguntas:
            pregunta.hacer_pregunta()
            participante.agregar_respuesta(pregunta.dimension, pregunta.respuesta)
        print("\n¡Test completado!")