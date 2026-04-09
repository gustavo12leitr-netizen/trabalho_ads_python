# Exercício 9: Cálculo de prestação em atraso
# Fórmula: Valor Final = Prestação + (Prestação * (Taxa/100) * Dias)

prestacao_atual = float(input("Digite o valor da prestação atrasada (R$): "))
taxa = float(input("Digite a taxa de juros diária (%): "))
dias = int(input("Digite a quantidade de dias em atraso: "))

# O enunciado pede a divisão por 100 para transformar a taxa em decimal
nova_prestacao = prestacao_atual + (prestacao_atual * (taxa / 100) * dias)

print(f"\nO valor atualizado da prestação é: R$ {nova_prestacao:.2f}")
