import spacy   #importamos spacy
import random  #importamos random
from spacy.tokens import Doc
from spacy.vocab import Vocab

def leer_texto(texto):
    with open(texto, 'r',encoding="latin-1") as text:
        return text.read()

#procesador = spacy.load('es_core_news_lg')
#texto = leer_texto("Sirena.txt")

#texto_procesado.to_disk("texto_procesado")
#procesador.to_disk("procesador")

#texto_procesado = nlp(texto)
texto_procesado = Doc(Vocab()).from_disk("texto_procesado")


"""
def NOMBRE_METODO():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'TIPO DE TAG'])
"""

def sustantivo_plural():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'NOUN__Gender=Masc|Number=Plur'])

def adjetivo_plural():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADJ__Gender=Masc|Number=Plur'])

def sust_sing_fem():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'NOUN__Gender=Fem|Number=Sing'])

def adj_sing_fem():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADJ__Gender=Fem|Number=Sing'])

def adj_sing_masc():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADJ__Gender=Masc|Number=Sing'])

def adverbio():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'ADV'])

def aux_plural_futuro():
    return random.choice([token.orth_ for token in texto_procesado if token.tag_ == 'AUX__Mood=Ind|Number=Plur|Person=3|Tense=Fut|VerbForm=Fin'])

"""

for x in range(4):

    print(f'Los {sustantivo_plural()} {adjetivo_plural()}')
    print(f'{adverbio()} seran')
    print(f'La {sust_sing_fem()} {adj_sing_fem()}')


file1 = open("resultado.txt","w",encoding="latin-1")
file1.write(resultado)
file1.close
"""
