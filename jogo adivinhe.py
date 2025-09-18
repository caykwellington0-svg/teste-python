import random

print("Bem-vindo ao advinhe o número")
print("As regras são simples, vou pensar em um número e você tentará adivinhá-lo")
numero = random.randint(1, 10)
isGuessRigth = False
while isGuessRigth != True:
    adivinha = input("Digite um número de 1 a 10:")
    if int(adivinha) == numero:
        print("Você adivinhou {}. O número está correto! Você ganhou!".format(adivinha))
        isGuessRight = True
    else:
        print("Você digitou o número {}. Desculpe, não é esse. Tente novamente.".format(adivinha))