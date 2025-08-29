print( "Olá, mundo!")

# programa: adivinhe o número
import random

print("Bem-vindo ao jogo de adivinhar o número!")

# O computador escohe o número de 1 a 5
numero_secreto= random.randint(1, 5)

#pedindo seu chute

chute = int(input("Tente adivinhar o número(1 a 5):"))

#comparando chute com número secreto

if chute == numero_secreto:
    print("Parabéns! Você acertou!")
else:
    print("Ops! Você errou. O número era " + str (numero_secreto) )
