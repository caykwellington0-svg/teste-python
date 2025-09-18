print("====CALCULADORA SIMPLES!====")
num1 = float(input("Digite o primeiro número:"))
num2 = float(input("Digite o segundo número"))
print("\nEscolha a operação: (+,-,*,/)")
operação = input("Digite a operação:")
if operação == "+":
    resultado = num1 + num2
elif operação == "-":
    resultado = num1 - num2
elif operação == "*":
    resultado = num1 * num2
elif operação == "/":
    resultado = num1 / num2
    if num2 !=0:
        resultado = num1 / num2
    else: 
        resultado = "não permitido divisão por zero! "

else:
    resultado = "Operação inválida!"
print( "\nResuItado:", resultado)
