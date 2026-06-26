from modelos import Pregunta

def cargar_preguntas():
    datos = [
        ("Disfruto explorar ideas nuevas o poco convencionales", "Apertura"),
        ("Tengo una imaginación muy activa", "Apertura"),
        ("Suelo planificar mis tareas con anticipación", "Responsabilidad"),
        ("Cumplo mis compromisos aunque sea aburrido", "Responsabilidad"),
        ("Me siento cómodo iniciando conversaciones con desconocidos", "Extroversión"),
        ("Prefiero estar rodeado de gente que estar solo", "Extroversión"),
        ("Me preocupo genuinamente por el bienestar de los demás", "Amabilidad"),
        ("Evito conflictos siempre que puedo", "Amabilidad"),
        ("Me estreso fácilmente ante imprevistos", "Neuroticismo"),
        ("Mis emociones cambian con frecuencia", "Neuroticismo"),
    ]
    return [Pregunta(texto, dimension) for texto, dimension in datos]