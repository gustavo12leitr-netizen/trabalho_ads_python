import math

# Exercício 6: Calcular a hipotenusa de um triângulo retângulo
cateto1 = float(input("Digite o valor do primeiro cateto: "))
cateto2 = float(input("Digite o valor do segundo cateto: "))

# Fórmula: Raiz quadrada da soma dos quadrados dos catetos
hipotenusa = math.sqrt(cateto1**2 + cateto2**2)

print(f"\nA hipotenusa do triângulo é: {hipotenusa:.2f}")
