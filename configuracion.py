class Configuracion:
    def __init__(self):
        # Tokens de Twitter
        self.api_key = '8uwasd9eVvEutiExvCCtFr2SVE'
        self.secret_api_key = 'J4N5VoHasdasd7Z4aFZ49q9dwud4jSoMhtT8mevNBjI4aItmMM6'
        self.access_token = '126467jkghj67jghjdfgdfAyKJMwb3iy7bHjlQ2wioy'
        self.secret_access_token = 'jV456dfhdfhebyWFQwW3ygQ3zip8u6vj7KGE4g'
        # Aca van las palabras que mirara el bot para saber si responde o no a un tweet
        self.palabras_para_responder = [' ','pregunta']
        # El tiempo de espera entre publicaciones y respuestas, esta en segundos
        self.tiempo_entre_publicaciones = 300
        # Aca se designa el nombre del archivo donde se guardaran los IDs de los Tweets ya respondidos
        self.archivo_texto = 'ids_reply.txt'
