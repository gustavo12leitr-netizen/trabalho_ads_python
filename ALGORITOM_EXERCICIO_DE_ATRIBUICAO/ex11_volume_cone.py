# Exercício 11: Cálculo do Volume de um Cone
# Fórmulas: Área da Base = 3.14 * R² | Volume = (Área da Base * Altura) / 3

raio = float(input("Digite o valor do raio do cone: "))
altura = float(input("Digite o valor da altura do cone: "))

# Calculando a área da base
pi = 3.14
area_base = pi * (raio ** 2)

# Calculando o volume (dividindo por 3 conforme o dado)
volume = (area_base * altura) / 3

print(f"\nA área da base do cone é: {area_base:.2f}")
print(f"O volume total do cone é: {volume:.2f}")
