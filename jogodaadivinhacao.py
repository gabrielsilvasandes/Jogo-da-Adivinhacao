import random
from time import sleep
print("=======  JOGO DA ADIVINHAÇÃO  =======")
print('-=' * 30)
print("Vou pensar em um Número entre 0 e 5. Tente adivinhar.... ")
print('-=' * 30)
numero = int(input("Em que número eu pensei?"))
lista = [1, 2, 3, 4, 5]
sortear = random.choice(lista)
sleep(0.8)
print("PROCESSANDO....")
sleep(1.0)
if numero != sortear:
    print(f"GANHEI! Eu pensei no número {sortear} e não no {numero}")
else:
    print("PARABÉNS! Você conseguiu me vencer!")


