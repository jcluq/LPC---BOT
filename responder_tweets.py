import tweepy
import time
import os
from configuracion import Configuracion
#from generador_tracery import texto_final
#import PLN_Generador as PLN


class Responder:
    def __init__(self,principal):
        # corre el API y verifica las llaves de acceso
        self.configuracion = principal.configuracion
        self.lista_de_ids = []
        self.lista_de_comandos = []
        self.bandera_copia = False


    def responder_tweets(self,api,palabras):
        # Cada tweeter tiene un idetificador unico, este lo podemos encontrar en el link del tweet
        # 'https://twitter.com/GigiBot8/status/1307389114636029953' >>>>>> id = '1307389114636029953'
        # o tambien podemos pedirlo al API con 'tweet.id'
        # Empezamos creando un lista vacia donde se archivaran temporalmente
        # los ID's de los tweets en los que nos etiqueten para responder
        self.lista_de_comandos = palabras
        self.lista_de_ids = []

        # Abrimos el archivo de texto donde guardaremos los ID's de los tweeters
        # que ya respondimos, asi evitamos que cada vez que el programa se reinicie
        # responda a todos los tweets

        with open(self.configuracion.archivo_texto,'r+') as texto_de_ids:
            primera_lista_ids = texto_de_ids.readlines()
            for ides in primera_lista_ids:
                self.lista_de_ids.append(ides.strip())

            # Este API usa la funcion Cursor como una iteracion entre datos, en este caso
            # le estamos diciendo que busque entre las menciones en la linea del tiempo
            # La funcion de pagina permite iterar solo entre la primera y segunda pagina de respuestas
            # Asi evitamos que revise todo el historico de tweets enviados
            # Cada pagina consta de 18 tweets
            for tweet in tweepy.Cursor(api.mentions_timeline, page = [1,2]).items():
                self.bandera = False
                # Aca revisa si el tweet es una respuesta directa o un comentario del tweet a responder_tweets
                # Si queremos que responda a comentarios dentro de una respuesta comentamos la linea 45 y 46
                if tweet.in_reply_to_status_id is not None:
                    continue
                # Asigna la bandera para saber si el tweet ya fue respondido
                for id in self.lista_de_ids:
                    if id == str(tweet.id):
                        self.bandera_copia = True
                # Aca se escriben las respuestas si se encuentra la palabra clave dentro de la publicacion
                if self.bandera_copia is False:
                    for comando in self.lista_de_comandos:
                        comparasion = (tweet.text.lower()).find(comando)
                        if comparasion == -1:
                            #if any(palabra in tweet.text.lower() for palabra in palabras):
                                # Seguimos a quien nos etiquete si aun no se le sigue
                            if not tweet.user.following:
                                tweet.user.follow()
                            # Extraemos el nombre del usuario del tweet
                            # y lo pegamos con un @ para que Twitter lo lea como un reply
                            usuarix = tweet.user.screen_name
                            ##### En caso de usar Tracery descomentar linea 64 :
                            #respuesta = "@" + str(usuarix) + ' ' + texto_final()
                            ##### En caso de usar PLN descomentar linea 66 y 67 :
                            #texto_generativo_PLN = f'{PLN.adjetivo_plural()} ejemplos para el {PLN.adj_sing_masc()} generador PLN :)'
                            #respuesta = "@" + str(usuarix) + ' ' + texto_generativo_PLN
                            # Aca se envia el mensaje a publicar
                            api.update_status(
                                status=respuesta,
                                in_reply_to_status_id=tweet.id,
                                )
                            time.sleep(2)
                                # Se archiva el ID unico del tweet en el archivo 'ids_reply.txt'
                                # Asi evitamos que cada vez que el programa empieze
                                    # solo responda a los Tweetest que no hemos respondido
                            texto_de_ids.write(str(tweet.id) + '\n')
        # Para mantener el log de ids de tweets ligero
        # Si hay mas de 60 ids guardados borrara los ultimos 20
        if len(self.lista_de_ids) >= 60:
            del self.lista_de_ids[:19]
            os.remove(self.configuracion.archivo_texto)
            with open(self.configuracion.archivo_texto, "w") as file:
                for ides_nuevos in self.lista_de_ids:
                    file.write(ides_nuevos + '\n')
