'''userReply = input("Você precisa enviar um pacote?(Digite SIM ou NÃO)")
if userReply == "SIM": print("Podemos ajuda-lo a enviar esse pacote!")
else:
    print("Volte quando precisar enviar um pacote")'''

usuario = input("Você deseja comprar selos, comprar envelope ou tirar uma cópia? (Selo, Envelope, Cópia)")
if usuario == "selo":
    print("Temos muitos designs para escolher")
elif usuario == "envelope":
    print("Temos varios tamanhos de envelopes para escolher")
elif usuario == "cópia":
    copias = input("Quantas cópias deseja fazer? (digite o número de cópias)")
    print("Aqui está {} cópias".format(copias))

else:
    print("Obrigado, volte outra hora!")

