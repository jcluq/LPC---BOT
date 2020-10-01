import tracery
import time
from tracery.modifiers import base_english

lista_de_objetos = ['reloj', 'piano', 'pescado', 'avion','lapiz','perro','machete','helado','taladro','borrador']
emojis = ['\U00002601','\U0001F468\U0000200D\U0001F467','\U0001f618','\U0001f629','\U0001F642']

with open('lugares.txt','r',encoding="utf-8") as texto_de_formas:
    lista_de_lugares = texto_de_formas.read().splitlines()

reglas = {
    'estructura_final': 'el #dia.capitalize# es como un #objeto# que #estado_y_lugar# #emojis#',
    'dia': ['lunes','martes','miercoles','jueves','viernes','sabado','domingo'],
    'objeto': lista_de_objetos,
    'estado_y_lugar': '#estado# en un #lugar#',
    'estado': ['tambalea','dibuja','llora','sonrie','rie','espera','escupe','flota'],
    'lugar': lista_de_lugares,
    'emojis': emojis}

grammar = tracery.Grammar(reglas)
grammar.add_modifiers(base_english)

def texto_final():
    return grammar.flatten("que le puedo decir ... #estructura_final#")

'''
while True:
    variable = texto_final()
    print(variable)
    time.sleep(3)
'''
resultado = texto_final()
print(resultado)
