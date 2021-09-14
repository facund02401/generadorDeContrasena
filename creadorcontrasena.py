import string
import random
from string import ascii_letters
from random import shuffle

letras = ascii_letters
numeros = string.digits
simbolos = string.punctuation[0:17]
respuesta1 = input('¿Queres una contraseña? (indique si o no)\n').upper()
respuesta = 'SI'

while respuesta == 'SI':

    while respuesta1 == 'SI':

        elecc_letras = int(
            input('¿Cuantas letras queres que tenga tu contraseña?\n'))
        elecc_numeros = int(
            input('¿Cuantos números queres en tu contraseña?\n'))
        elecc_simbolos = int(
            input('¿Cuantos símbolos queres en tu contraseña?\n'))

        contrasena = random.sample(letras, elecc_letras) + random.sample(
            numeros, elecc_numeros) + random.sample(simbolos, elecc_simbolos)
        shuffle(contrasena)
        contra2 = ''.join(contrasena)
        print(f'Tu contraseña aleatorizada es: {contra2}')

        break
    respuesta = input('\nQueres otra contraseña? (indique si o no)\n').upper()
