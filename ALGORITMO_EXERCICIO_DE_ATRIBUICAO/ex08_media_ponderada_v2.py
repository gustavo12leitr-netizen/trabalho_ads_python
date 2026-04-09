# Exercício 8: Cálculo de Média Ponderada (Pesos 7, 3, 4, 2)
a = int(input("Digite o valor de A: "))
b = int(input("Digite o valor de B: "))
c = int(input("Digite o valor de C: "))
d = int(input("Digite o valor de D: "))

# Fórmula: (A*7 + B*3 + C*4 + D*2) dividido por 16
media = (a * 7 + b * 3 + c * 4 + d * 2) / 16

print(f"\nA média ponderada (v2) é: {media:.2f}")
