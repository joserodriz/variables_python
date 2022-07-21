# Tipos de variables [Python]
# Ejercicios de profundización

# Autor: Inove Coding School
# Version: 2.0

# NOTA: 
# Estos ejercicios son de mayor dificultad que los de clase y práctica.
# Están pensados para aquellos con conocimientos previo o que dispongan
# de mucho más tiempo para abordar estos temas por su cuenta.
# Requiere mayor tiempo de dedicación e investigación autodidacta.

# IMPORTANTE: NO borrar los comentarios en VERDE o NARANJA

# Ejercicios de práctica con números
'''
Enunciado:
Realice un calculadora, se ingresará por línea de comando dos
números reales y se deberá calcular todas las operaciones entre ellos:
A) Suma
B) Resta
C) Multiplicación
D) División
E) Exponente/Potencia

- Para todos los casos se debe imprimir en pantalla el resultado aclarando
  la operación realizada en cada caso y con que números
  se ha realizado la operación
  ej: La suma entre 4.2 y 6.5 es 10.7
'''

from math import exp
from statistics import multimode


print('¡Nuestra primera calculadora!')
# Empezar aquí la resolución del ejercicio
numero_1 = float(input())
numero_2 = float(input())

suma = numero_1 + numero_2
resta = numero_1 - numero_2
mult = numero_1 * numero_2
divis = numero_1 / numero_2
potencia = numero_1 ** numero_2

print('La suma de', numero_1, 'y', numero_2, 'es', suma)
print('La resta de', numero_1, 'y', numero_2, 'es', resta)
print('La multiplicacion de', numero_1, 'y', numero_2, 'es', mult)
print('La division entre', numero_1, 'y', numero_2, 'es', divis)
print('La potencia entre', numero_1, 'y', numero_2, 'es', potencia)
