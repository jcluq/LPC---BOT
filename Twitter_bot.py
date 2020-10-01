import tweepy
import time
import os
import random
from configuracion import Configuracion
from responder_tweets import Responder
#from generador_tracery import texto_final
#import PLN_Generador as PLN



class Tweetest:
    def __init__(self):
        # corre el API y verifica las llaves de acceso
        self.configuracion = Configuracion()
        auth = tweepy.OAuthHandler(self.configuracion.api_key, self.configuracion.secret_api_key)
        auth.set_access_token(self.configuracion.access_token, self.configuracion.secret_access_token)
        self.api = tweepy.API(auth)
        self.bandera_autentificacion = self.api.verify_credentials()
        # aca se vincula el programa que responde a los tweets
        self.responder= Responder(self)


    def _seguir_seguidores(self):
        # Esta funcion sigue a quienes nos sigan
        # Este API usa la funcion Cursor como una iteracion entre datos, en este caso
        # le estamos diciendo que busque entre nuestros seguidores
        for follower in tweepy.Cursor(self.api.followers).items():
            if not follower.following:
                follower.follow()

    def programa(self):
        # Aca es donde corren todas las funciones
        # Revisa que las llaves este correctas para empezar a correr
        if self.bandera_autentificacion is not False:
            print('Autentificacion correcta')
            while True:
                # Corre la funcion de seguir a quienes nos sigan
                self._seguir_seguidores()
                # Aca se responden los tweets si alguno de las palabras que contiene
                # coinciden con las palabras seleccionadas en el archivo de configuracion
                # En este caso la palabra 'ayuda' o  'pregunta'
                since_id = self.responder.responder_tweets(self.api,self.configuracion.palabras_para_responder)
                # Se define que tanto tiempo pasara entre cada publicacion del Bot
                # y que cada tanto responde y sigue personas
                ##### ACA VA LA FUNCION DEL TEXTO GENERATIVO segun el metodo
                ## PARA PLN descomentar::
                #texto_generativo_PLN = f'{PLN.adjetivo_plural()} ejemplos para el {PLN.adj_sing_masc()} generador PLN :)'
                #self.api.update_status(texto_generativo_PLN)
                ### PARA Tracery descomentar::
                #self.api.update_status(texto_final())
                time.sleep(self.configuracion.tiempo_entre_publicaciones)
                print('y zas, iteracion')

test = Tweetest()
test.programa()
