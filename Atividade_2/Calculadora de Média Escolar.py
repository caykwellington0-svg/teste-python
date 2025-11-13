'''Crie um programa que calcula a média escolar de um aluno. Use as seguintes notas:

* Nota 1: 7.5
* Nota 2: 8.0
* Nota 3: 6.5
O programa deve calcular a média e exibir todas as notas e o resultado final, arredondando para duas casas decimais.'''

nome_produto = "Camiseta"
preco_original = 50.00
porc_desconto = 20

valor_desconto = preco_original * (porc_desconto / 100)
preco_final = preco_original - valor_desconto

print("Produto:", nome_produto)
print("Preço original: R$", preco_original)
print("Desconto:", porc_desconto, "%")
print("Valor do desconto: R$", round(valor_desconto, 2))
print("Preço final: R$", round(preco_final, 2))